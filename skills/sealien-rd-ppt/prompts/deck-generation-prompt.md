# AI Deck Generation Prompt Template

Use the Sealien Robotics Innovation R&D Visual Design System (`Sealien-RD-DesignSystem`) to build an engineering/research presentation:

1. **Source Inputs**: [List your markdown notes, experimental CSV/JSON metrics, figure PNG/SVGs, and sea-trial/hardware images].
2. **Design System Constraints**:
   - Follow `skills/sealien-rd-ppt/SKILL.md`, `brand/colors.json`, and `brand/typography.json`.
   - Instantiate slides from `templates/powerpoint/Sealien_RD_Master_V4.1.0.pptx` using layouts `01`–`21` in `skills/sealien-rd-ppt/references/layout-catalog.md`.
   - Use conclusion-first slide titles (Assertion-Evidence format) and include units, operating conditions, and data sources on every plot.
   - Output file naming: `项目名称_汇报主题_YYYYMMDD_Vx.y.z.pptx`.
3. **Validation Gate**:
   - Run `python automation/validate_ppt.py <output.pptx>`.
   - Render slides and visually inspect for text overflow, overlap, or distorted aspect ratios before finishing.
