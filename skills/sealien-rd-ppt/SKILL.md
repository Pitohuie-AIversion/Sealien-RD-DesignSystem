---
name: sealien-rd-ppt
description: Generates and validates Sealien Robotics Innovation R&D Center presentations using the V4.1.0 design system, 21 standard 16:9 layouts, 60 editable vector components, and brand tokens.
---

# Sealien R&D Visual Design System Skill

Use this skill whenever generating, editing, or reviewing presentations, technical architecture decks, or milestone reports for the **Sealien Robotics Innovation R&D Center (创新研发中心)**.

## 1. Canonical Assets

Read these files before creating or editing slides:
- **Brand Tokens**: `brand/colors.json` and `brand/typography.json`
- **Master Template**: `templates/powerpoint/Sealien_RD_Template_V4.1.0.potx` (or `templates/powerpoint/Sealien_RD_Master_V4.1.0.pptx` when manipulating slides programmatically with `python-pptx`, remembering to strip sample slides before populating new ones)
- **Component Library**: `components/Sealien_RD_Components_V4.1.0.pptx` (60 editable vector groups across 10 pages)
- **Layout Catalog**: `skills/sealien-rd-ppt/references/layout-catalog.md`
- **Design & Evidence Rules**: `guidelines/design-guidelines.md` and `guidelines/presentation-guidelines.md`

## 2. Hard Constraints

1. **Slide Size & Fonts**: Strictly `16:9` (`13.333 × 7.5 in`), Chinese in `Microsoft YaHei`, Latin/numbers in `Arial`. Do not bundle font files.
2. **Colors**: Use `#0033CC` (Brand Blue), `#002699` (Deep Blue), `#001760` (Navy Blue), `#E1E9FF` (Light Blue), `#FFFFFF` (White), and `#47588D` (Muted Indigo) for UI structure. Select scientific colormaps (e.g., `viridis`, `cividis`, `RdBu`) by physical meaning for quantitative heatmaps and flow fields.
3. **Assertion-Evidence Titles**: Every content slide title states a concrete conclusion or finding, not a generic noun phrase.
4. **Placeholder Integrity & Shape IDs**:
   - Preserve layout placeholders (`TITLE`, `BODY`, `OBJECT`, `CHART`, `PICTURE`, `TABLE`, `SLIDE_NUMBER`).
   - Keep every `p:cNvPr/@id` in `[1, 2147483647]` (Microsoft PowerPoint rejects IDs `> 2147483647`).
5. **Scientific Honesty**: Distinguish `示意` (illustrative) vs `实测` (measured), label physical quantities, units, conditions, and error sources, and never pass generic robotics icons off as real hardware photos.

## 3. Workflow

1. Plan slide-by-slide outline and map each slide to a layout `01`–`21` in `references/layout-catalog.md`.
2. Instantiate from `templates/powerpoint/Sealien_RD_Master_V4.1.0.pptx` (removing template example slides after reading layout references) and name output `项目名称_汇报主题_YYYYMMDD_Vx.y.z.pptx`.
3. Insert real charts/tables/images into native placeholders; reuse vector stencils from `components/Sealien_RD_Components_V4.1.0.pptx` only as conceptual building blocks.
4. Validate generated `.pptx` with:
   ```bash
   python automation/validate_ppt.py path/to/output.pptx
   ```
   and visually inspect rendered slide PNGs before final delivery.
