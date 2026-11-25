# Design Guidelines — Sealien Innovation R&D Center (V4.1.0)

## 1. Brand Color System

Source of truth: [`brand/colors.json`](../brand/colors.json) and [`brand/theme/color_scheme.xml`](../brand/theme/color_scheme.xml).

| Token | Hex | Theme Slot | Usage |
| :--- | :--- | :--- | :--- |
| Brand Blue | `#0033CC` | `accent1` | Primary brand identity, header bar, key highlights |
| Deep Blue | `#002699` | `primary_dark` | Table headers, secondary cover panels, dark emphasis |
| Navy Blue | `#001760` | `dk2` | Primary headings, section titles, high-contrast body text |
| Light Blue | `#E1E9FF` | `lt2` | Soft canvas tint, alternating table rows, node fill |
| White | `#FFFFFF` | `lt1` | Primary slide background, reversed text on blue surfaces |
| Muted Indigo | `#47588D` | `ui_neutral` | Subtitles, footers, captions, slide numbers |
| Hairline Blue | `#C9D4F4` | `ui_border` | Divider lines and subtle borders |

### Scientific Colormap Policy
- Keep brand blues for structural UI, headers, and schematic diagrams.
- **Do not** force scientific heatmaps, flow fields, vorticity contours, or error maps into brand monochrome if it obscures physical polarity or magnitude. Choose perceptually uniform or diverging scientific colormaps (e.g., `viridis`, `cividis`, `RdBu`) appropriate to the physical quantity, and always show a labeled colorbar with units.

## 2. Typography & Canvas

Source of truth: [`brand/typography.json`](../brand/typography.json) and [`brand/theme/font_scheme.xml`](../brand/theme/font_scheme.xml).

- **Canvas**: `16:9` widescreen (`13.333 × 7.5 in` / `12192000 × 6858000 EMU`).
- **Fonts**:
  - Chinese / East Asian: `Microsoft YaHei` (微软雅黑)
  - Latin / Numeric: `Arial`
  - **Distribution rule**: Team computers must have `Microsoft YaHei` and `Arial` installed; templates do not embed or redistribute font binaries.
- **Type Scale**:
  - Cover title: `36–44 pt`
  - Slide title: `26–32 pt`
  - Regular body text: `18–24 pt`
  - Chart annotations & labels: `>= 14 pt` wherever possible
  - Footer & slide number: `11 pt`

## 3. Brand Media Integrity

- [`brand/logos/sealien_logo.png`](../brand/logos/sealien_logo.png) and [`brand/backgrounds/original_brand_gradient.png`](../brand/backgrounds/original_brand_gradient.png) must remain byte-identical to the canonical V4.0/V4.1 assets.
- Do not stretch, recolor, crop, or distort the Sealien Robotics logo (`noChangeAspect="1"`).

## 4. Accessibility & Clarity

- Preserve native title placeholders (`TITLE`) and alt-text (`descr`) on brand images and reusable vector groups.
- Never encode pass/fail/warning state by color alone — pair color with text badges, icons, or pattern/line style.
- Run PowerPoint `Review -> Check Accessibility` (`审阅 -> 检查辅助功能`) on final project decks before formal distribution.
