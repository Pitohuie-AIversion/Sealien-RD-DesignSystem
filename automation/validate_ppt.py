"""Validate Sealien-RD-DesignSystem OOXML packages, brand integrity, manifest, and PDF fonts."""

from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

INT32_MAX = 2_147_483_647


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def validate_ooxml_package(
    pkg_path: Path,
    expected_brand_hashes: dict[str, str] | None = None,
) -> list[str]:
    """Validate ZIP integrity, XML syntax, .rels targets, INT32 cNvPr IDs, and brand media."""
    errors: list[str] = []
    if not pkg_path.exists():
        return [f"Missing package: {pkg_path}"]

    try:
        with zipfile.ZipFile(pkg_path, "r") as zf:
            corrupt = zf.testzip()
            if corrupt is not None:
                errors.append(f"{pkg_path}: corrupt zip member {corrupt}")
                return errors

            names = set(zf.namelist())
            for name in sorted(names):
                if name.endswith((".xml", ".rels")):
                    try:
                        root = ET.fromstring(zf.read(name))
                    except ET.ParseError as exc:
                        errors.append(f"{pkg_path}:{name}: XML parse error: {exc}")
                        continue

                    if name.endswith(".rels"):
                        part_dir = name.split("/_rels/")[0] if "/_rels/" in name else ""
                        for rel in root:
                            if rel.attrib.get("TargetMode") == "External":
                                continue
                            tgt = rel.attrib.get("Target", "")
                            if not tgt:
                                continue
                            resolved = (
                                tgt.lstrip("/")
                                if name == "_rels/.rels" or tgt.startswith("/")
                                else posixpath.normpath(posixpath.join(part_dir, tgt))
                            )
                            if resolved not in names:
                                errors.append(f"{pkg_path}:{name}: broken relationship target {tgt} -> {resolved}")

                    # Check PowerPoint signed INT32 cNvPr/@id safety and per-part uniqueness
                    seen_ids: dict[int, str] = {}
                    for el in root.iter():
                        if el.tag.endswith("cNvPr"):
                            raw_id = el.attrib.get("id")
                            if raw_id is None:
                                errors.append(f"{pkg_path}:{name}: cNvPr missing id attribute")
                                continue
                            try:
                                vid = int(raw_id)
                            except ValueError:
                                errors.append(f"{pkg_path}:{name}: non-integer cNvPr id={raw_id!r}")
                                continue
                            if vid < 1 or vid > INT32_MAX:
                                errors.append(
                                    f"{pkg_path}:{name}: cNvPr id={vid} ({el.attrib.get('name', '')}) "
                                    f"outside PowerPoint signed INT32 range [1, {INT32_MAX}]"
                                )
                            if vid in seen_ids:
                                errors.append(
                                    f"{pkg_path}:{name}: duplicate cNvPr id={vid} "
                                    f"({seen_ids[vid]!r} vs {el.attrib.get('name', '')!r})"
                                )
                            else:
                                seen_ids[vid] = el.attrib.get("name", "")

            if expected_brand_hashes and pkg_path.suffix.lower() in {".pptx", ".potx"}:
                for media_rel, expected_hash in expected_brand_hashes.items():
                    if media_rel not in names:
                        errors.append(f"{pkg_path}: missing required brand media {media_rel}")
                    else:
                        actual_hash = sha256_bytes(zf.read(media_rel))
                        if actual_hash != expected_hash:
                            errors.append(
                                f"{pkg_path}:{media_rel}: hash mismatch (expected {expected_hash}, got {actual_hash})"
                            )
    except zipfile.BadZipFile as exc:
        errors.append(f"{pkg_path}: invalid ZIP/OOXML container: {exc}")

    return errors


def validate_pdf_fonts(pdf_path: Path) -> list[str]:
    """Verify PDF opens cleanly and embeds fonts (avoiding unembedded CID fonts like bare STSong-Light)."""
    errors: list[str] = []
    if not pdf_path.exists():
        return [f"Missing PDF: {pdf_path}"]
    try:
        import pypdf
    except ImportError:
        return [f"Cannot validate PDF fonts ({pdf_path}): pypdf is not installed"]

    reader = pypdf.PdfReader(str(pdf_path))
    if len(reader.pages) == 0:
        return [f"{pdf_path}: PDF has 0 pages"]

    for page_idx, page in enumerate(reader.pages, start=1):
        resources = page.get("/Resources", {})
        fonts = resources.get("/Font", {})
        if not fonts:
            errors.append(f"{pdf_path}: page {page_idx} has no font dictionary")
            continue
        for key, ref in fonts.items():
            obj = ref.get_object()
            base_font = str(obj.get("/BaseFont", ""))
            has_descriptor = "/FontDescriptor" in obj
            has_descendants = "/DescendantFonts" in obj
            if has_descendants:
                desc = obj["/DescendantFonts"][0].get_object()
                desc_fd = desc.get("/FontDescriptor")
                if desc_fd is None:
                    errors.append(f"{pdf_path}: page {page_idx} font {key} ({base_font}) missing descendant FontDescriptor")
                else:
                    fd_obj = desc_fd.get_object()
                    if not any(k in fd_obj for k in ("/FontFile", "/FontFile2", "/FontFile3")):
                        errors.append(f"{pdf_path}: page {page_idx} font {key} ({base_font}) is NOT embedded")
            elif not has_descriptor:
                errors.append(f"{pdf_path}: page {page_idx} font {key} ({base_font}) missing FontDescriptor")
    return errors


def validate_manifest(repo_root: Path) -> list[str]:
    """Check ASSET_MANIFEST.json entries match actual file sizes and SHA-256 digests."""
    manifest_path = repo_root / "ASSET_MANIFEST.json"
    if not manifest_path.exists():
        return [f"Missing manifest: {manifest_path}"]

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for entry in data.get("assets", []):
        rel = entry["path"]
        target = repo_root / rel
        if not target.exists():
            errors.append(f"Manifest entry missing on disk: {rel}")
            continue
        size = target.stat().st_size
        digest = sha256_file(target)
        if size != entry.get("size_bytes"):
            errors.append(f"Manifest size mismatch for {rel}: expected {entry.get('size_bytes')}, got {size}")
        if digest != entry.get("sha256"):
            errors.append(f"Manifest SHA-256 mismatch for {rel}: expected {entry.get('sha256')}, got {digest}")
    return errors


def validate_repository(repo_root: Path) -> list[str]:
    errors: list[str] = []

    logo = repo_root / "brand" / "logos" / "sealien_logo.png"
    grad = repo_root / "brand" / "backgrounds" / "original_brand_gradient.png"
    if not logo.exists() or not grad.exists():
        return [f"Missing brand media files under {repo_root / 'brand'}"]

    expected_brand = {
        "ppt/media/sealien_logo.png": sha256_file(logo),
        "ppt/media/original_brand_gradient.png": sha256_file(grad),
    }

    for json_rel in ("brand/colors.json", "brand/typography.json", "validation/structural_validation.json"):
        jp = repo_root / json_rel
        if not jp.exists():
            errors.append(f"Missing JSON spec: {json_rel}")
        else:
            try:
                json.loads(jp.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON in {json_rel}: {exc}")

    for pkg in [
        repo_root / "templates" / "powerpoint" / "Sealien_RD_Template_V4.1.0.potx",
        repo_root / "templates" / "powerpoint" / "Sealien_RD_Master_V4.1.0.pptx",
        repo_root / "components" / "Sealien_RD_Components_V4.1.0.pptx",
        repo_root / "brand" / "theme" / "Sealien_RD_Theme_V4.1.0.thmx",
    ]:
        errors.extend(validate_ooxml_package(pkg, expected_brand))

    errors.extend(validate_pdf_fonts(repo_root / "guidelines" / "Sealien_RD_UserGuide_V4.1.0.pdf"))
    errors.extend(validate_manifest(repo_root))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Sealien-RD-DesignSystem assets or custom decks.")
    parser.add_argument("targets", nargs="*", help="Optional specific .pptx/.potx/.thmx files to validate.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Path to Sealien-RD-DesignSystem root.",
    )
    args = parser.parse_args(argv)

    if args.targets:
        errors: list[str] = []
        for t in args.targets:
            errors.extend(validate_ooxml_package(Path(t)))
    else:
        errors = validate_repository(args.repo_root)

    if errors:
        print(f"VALIDATION FAILED ({len(errors)} error(s)):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED: all checked OOXML packages, brand media hashes, manifest digests, and PDF fonts OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
