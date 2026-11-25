# Changelog

All notable changes to the Sealien Robotics Innovation R&D Visual Design System are documented in this file.

## [V4.1.0] - 2026-11-25 (Initial Stable Release)

### Added
- **21 standard 16:9 presentation layouts** in `templates/powerpoint/Sealien_RD_Template_V4.1.0.potx` and `Sealien_RD_Master_V4.1.0.pptx` (expanded from 16 layouts in V4.0), including specialized layouts (`11`–`16`, `18`–`21`) for software matrices, neural architectures, flow-field validation, robotics system decomposition, IP portfolios, TRL acceptance, multi-panel figures, and photo covers.
- **60 editable vector component groups** across 10 categories in `components/Sealien_RD_Components_V4.1.0.pptx` (expanded from 36 components).
- **Native PowerPoint theme package** `brand/theme/Sealien_RD_Theme_V4.1.0.thmx` exported from Windows Microsoft PowerPoint 16 (`ppSaveAsOpenXMLTheme=31`) and verified via `ApplyTheme`.
- **Machine-readable design tokens & manifest**: `brand/colors.json`, `brand/typography.json`, `ASSET_MANIFEST.json`, and `validation/structural_validation.json`.
- **Automation & AI workflow**: `automation/validate_ppt.py`, `automation/build_release.py`, `.github/workflows/validate-assets.yml`, and `skills/sealien-rd-ppt/`.

### Fixed (Pre-Release Acceptance Pass)
- **Microsoft PowerPoint 16 compatibility (`0x80070570` fix)**: Fixed `ppt/slideMasters/slideMaster1.xml` slide-number placeholder `<p:cNvPr id="2147483671">` (exceeding signed 32-bit int max `2147483647`, which caused Microsoft PowerPoint 16 to reject `.potx`/`.pptx` files as corrupted) to `id="2"` across template, master, and component decks.
- **User Guide PDF Chinese rendering**: Replaced unembedded CID-font PDF (`STSong-Light`) with an embedded-font (`MicrosoftYaHei`, `ArialMT`) 3-page PDF (`guidelines/Sealien_RD_UserGuide_V4.1.0.pdf`) so Chinese glyphs render consistently across Windows, macOS, browsers, and Linux viewers.
- **Package status**: Updated `docProps/core.xml` and `docProps/custom.xml` document status from `Draft` to `Released`.

### Preserved
- Original `brand/logos/sealien_logo.png` and `brand/backgrounds/original_brand_gradient.png` preserved byte-for-byte; V4.0 brand color palette strictly inherited.
