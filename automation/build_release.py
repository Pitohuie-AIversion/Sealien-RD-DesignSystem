"""Build deterministic Release assets, AssetPack ZIP, and SHA256SUMS.txt."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import zipfile
from pathlib import Path

FIXED_ZIP_TIME = (2026, 11, 25, 0, 0, 0)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_deterministic_zip(files: list[tuple[Path, str]], out_zip: Path) -> None:
    """Create a reproducible ZIP archive with normalized timestamps and permissions."""
    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for src, arcname in sorted(files, key=lambda pair: pair[1]):
            info = zipfile.ZipInfo(filename=arcname, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, src.read_bytes())


def build_release(repo_root: Path, version: str) -> Path:
    out_dir = repo_root / "dist" / version
    out_dir.mkdir(parents=True, exist_ok=True)

    release_files = [
        (repo_root / "templates" / "powerpoint" / f"Sealien_RD_Template_{version}.potx", f"Sealien_RD_Template_{version}.potx"),
        (repo_root / "templates" / "powerpoint" / f"Sealien_RD_Master_{version}.pptx", f"Sealien_RD_Master_{version}.pptx"),
        (repo_root / "components" / f"Sealien_RD_Components_{version}.pptx", f"Sealien_RD_Components_{version}.pptx"),
        (repo_root / "brand" / "theme" / f"Sealien_RD_Theme_{version}.thmx", f"Sealien_RD_Theme_{version}.thmx"),
        (repo_root / "guidelines" / f"Sealien_RD_UserGuide_{version}.pdf", f"Sealien_RD_UserGuide_{version}.pdf"),
    ]

    for src, dst_name in release_files:
        if not src.exists():
            raise FileNotFoundError(f"Required release artifact not found: {src}")
        shutil.copy2(src, out_dir / dst_name)

    zip_entries: list[tuple[Path, str]] = [
        (repo_root / "README.md", f"Sealien_RD_AssetPack_{version}/README.md"),
        (repo_root / "CHANGELOG.md", f"Sealien_RD_AssetPack_{version}/CHANGELOG.md"),
        (repo_root / "ASSET_MANIFEST.json", f"Sealien_RD_AssetPack_{version}/ASSET_MANIFEST.json"),
        (repo_root / "templates" / "powerpoint" / f"Sealien_RD_Template_{version}.potx", f"Sealien_RD_AssetPack_{version}/01_templates/Sealien_RD_Template_{version}.potx"),
        (repo_root / "templates" / "powerpoint" / f"Sealien_RD_Master_{version}.pptx", f"Sealien_RD_AssetPack_{version}/01_templates/Sealien_RD_Master_{version}.pptx"),
        (repo_root / "components" / f"Sealien_RD_Components_{version}.pptx", f"Sealien_RD_AssetPack_{version}/02_components/Sealien_RD_Components_{version}.pptx"),
        (repo_root / "brand" / "logos" / "sealien_logo.png", f"Sealien_RD_AssetPack_{version}/03_brand/sealien_logo.png"),
        (repo_root / "brand" / "backgrounds" / "original_brand_gradient.png", f"Sealien_RD_AssetPack_{version}/03_brand/original_brand_gradient.png"),
        (repo_root / "brand" / "colors.json", f"Sealien_RD_AssetPack_{version}/03_brand/colors.json"),
        (repo_root / "brand" / "typography.json", f"Sealien_RD_AssetPack_{version}/03_brand/typography.json"),
        (repo_root / "brand" / "theme" / f"Sealien_RD_Theme_{version}.thmx", f"Sealien_RD_AssetPack_{version}/03_brand/Sealien_RD_Theme_{version}.thmx"),
        (repo_root / "brand" / "theme" / "theme1.xml", f"Sealien_RD_AssetPack_{version}/03_brand/theme1.xml"),
        (repo_root / "brand" / "theme" / "color_scheme.xml", f"Sealien_RD_AssetPack_{version}/03_brand/color_scheme.xml"),
        (repo_root / "brand" / "theme" / "font_scheme.xml", f"Sealien_RD_AssetPack_{version}/03_brand/font_scheme.xml"),
        (repo_root / "guidelines" / f"Sealien_RD_UserGuide_{version}.pdf", f"Sealien_RD_AssetPack_{version}/04_guidelines/Sealien_RD_UserGuide_{version}.pdf"),
        (repo_root / "validation" / "structural_validation.json", f"Sealien_RD_AssetPack_{version}/04_guidelines/structural_validation.json"),
        (repo_root / "previews" / "layouts.png", f"Sealien_RD_AssetPack_{version}/05_previews/layouts.png"),
        (repo_root / "previews" / "components.png", f"Sealien_RD_AssetPack_{version}/05_previews/components.png"),
    ]
    zip_path = out_dir / f"Sealien_RD_AssetPack_{version}.zip"
    write_deterministic_zip(zip_entries, zip_path)

    checksum_lines = []
    for artifact in sorted(p for p in out_dir.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt"):
        checksum_lines.append(f"{sha256_file(artifact)}  {artifact.name}")
    (out_dir / "SHA256SUMS.txt").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    return out_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Build release bundle and SHA256SUMS.txt.")
    parser.add_argument("--version", default="V4.1.0", help="Release version tag (default: V4.1.0).")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Path to Sealien-RD-DesignSystem root.",
    )
    args = parser.parse_args()
    out_dir = build_release(args.repo_root, args.version)
    print(f"Built release artifacts in: {out_dir}")
    for p in sorted(out_dir.iterdir()):
        print(f"  {p.name:40s} {p.stat().st_size:>10d} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
