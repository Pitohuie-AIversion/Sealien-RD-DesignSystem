# Release Checklist — Sealien-RD-DesignSystem

Run through every item before tagging a Release or syncing assets to SharePoint / Feishu / Internal NAS:

- [ ] **Automated OOXML & Asset Validation**: Run `python automation/validate_ppt.py` and verify exit code `0`:
  - ZIP integrity (`testzip()`) and XML well-formedness across `.potx`, `.pptx`, `.thmx`.
  - All `.rels` internal targets resolve cleanly.
  - All `p:cNvPr/@id` values satisfy `1 <= id <= 2147483647` (signed INT32 safe for Windows Microsoft PowerPoint) and are unique per part.
  - `brand/logos/sealien_logo.png` and `brand/backgrounds/original_brand_gradient.png` match canonical SHA-256 hashes inside `templates/powerpoint/` and `components/`.
  - `ASSET_MANIFEST.json` file sizes and SHA-256 hashes match working tree.
  - `guidelines/Sealien_RD_UserGuide_*.pdf` has embedded fonts (`MicrosoftYaHei` / `ArialMT`) so CJK text renders without blank glyphs.
- [ ] **Native Windows Microsoft PowerPoint Verification**:
  - Double-click / open `.potx` as a new untitled deck; confirm 21 layouts instantiate cleanly.
  - Add a new slide from a body layout, reorder slides, save and reopen `.pptx`, and verify native slide numbers (`idx=90`) recalculate properly.
  - Verify `.thmx` exports cleanly (`ppSaveAsOpenXMLTheme=31`) and `ApplyTheme` works on a fresh deck.
  - Check `Review -> Check Accessibility` on updated master/component slides.
- [ ] **Visual Previews & Documentation**:
  - Refresh `previews/layouts.png` and `previews/components.png` if slides changed.
  - Update `CHANGELOG.md`, `validation/structural_validation.json`, and `docProps` `Released` status.
- [ ] **Security & Confidentiality Review**:
  - Confirm no unpublished patents, customer info, real sea-trial logs, or sensitive project names entered templates or examples.
- [ ] **Release Build & Distribution**:
  - Run `python automation/build_release.py --version <VERSION>` to generate `dist/<VERSION>/` and `SHA256SUMS.txt`.
  - Upload Release assets to GitHub/GitLab Release, then sync the audited bundle to SharePoint / Feishu / NAS.
