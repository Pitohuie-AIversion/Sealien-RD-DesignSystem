# Automation Scripts

- **`validate_ppt.py`**: Validates OOXML integrity (`.potx`, `.pptx`, `.thmx`), internal `.rels` targets, signed-INT32 `p:cNvPr/@id` compatibility (`1..2147483647`), per-part shape ID uniqueness, byte-identical brand media hashes, `ASSET_MANIFEST.json` integrity, and embedded fonts in `guidelines/Sealien_RD_UserGuide_*.pdf`.
  - Default repo check: `python automation/validate_ppt.py`
  - Validate an additional deck: `python automation/validate_ppt.py path/to/deck.pptx`
- **`build_release.py`**: Builds a deterministic release directory (`dist/<VERSION>/`) containing the template, master, component library, native `.thmx` theme, User Guide PDF, consolidated ZIP archive (`Sealien_RD_AssetPack_<VERSION>.zip`), and `SHA256SUMS.txt`.
  - Run: `python automation/build_release.py --version V4.1.0`
