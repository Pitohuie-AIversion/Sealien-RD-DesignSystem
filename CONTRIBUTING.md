# Contributing to Sealien-RD-DesignSystem

Thank you for maintaining the Innovation R&D Center's visual design system.

## Contribution Rules

1. **Maintain the master, regenerate the template**:
   - Edit `templates/powerpoint/Sealien_RD_Master_V4.1.0.pptx` in Windows Microsoft PowerPoint (never edit `Sealien_RD_Template_V4.1.0.potx` independently without syncing both).
   - Export updated `.potx` and `.thmx` (`Design -> Themes -> Save Current Theme`) from the master deck so layouts, theme XML, and media stay synchronized.
2. **Preserve brand integrity**:
   - Do not modify `brand/logos/sealien_logo.png` or `brand/backgrounds/original_brand_gradient.png` without brand approval.
   - Keep `Microsoft YaHei` (CJK) and `Arial` (Latin/numeric) without bundling proprietary font binaries.
   - Keep `p:cNvPr/@id` values strictly within `1 .. 2147483647` (signed INT32 range required by Microsoft PowerPoint).
3. **Update previews & documentation**:
   - Refresh `previews/layouts.png` and `previews/components.png` whenever layouts or components change.
   - Update `CHANGELOG.md`, `ASSET_MANIFEST.json`, and `guidelines/Sealien_RD_UserGuide_V4.1.0.pdf` if usage changes.
4. **Run automated checks before opening a PR**:
   ```bash
   python automation/validate_ppt.py
   ```
   And verify the `.potx` opens as a new presentation in Windows Microsoft PowerPoint, slide numbers recalculate on reorder, and `Review -> Check Accessibility` shows no critical regressions.
