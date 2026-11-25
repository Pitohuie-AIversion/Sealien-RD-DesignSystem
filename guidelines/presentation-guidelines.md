# Presentation Guidelines — IRDC-PPT-001 (V4.1.0)

## 1. Choosing the Right Artifact

| File | Audience | Usage |
| :--- | :--- | :--- |
| `templates/powerpoint/Sealien_RD_Template_V4.1.0.potx` | All R&D presenters | Double-click or use `File -> New` to create a project deck. |
| `templates/powerpoint/Sealien_RD_Master_V4.1.0.pptx` | Template maintainers | Edit slide master, layouts, or placeholders; never overwrite for project decks. |
| `components/Sealien_RD_Components_V4.1.0.pptx` | All R&D presenters | Copy individual component groups (`01`–`60`), paste, and ungroup (`Ctrl+Shift+G`) to customize. |
| `brand/theme/Sealien_RD_Theme_V4.1.0.thmx` | PowerPoint users | Apply via `Design -> Themes` to restyle compatible decks. |

## 2. File Naming & Collaboration

- **Recommended project filename**: `项目名称_汇报主题_YYYYMMDD_Vx.y.z.pptx`
- Save project presentations separately; never modify shared team master files directly.
- Delete unused sample slides after instantiating the layouts you need (`17 空白｜完全自由画布` is intentionally blank for custom compositions).

## 3. Slide Numbers & Placeholders

- Body layouts (`02`, `04`–`09`, `11`–`16`, `18`–`20`) include a native `SLIDE_NUMBER` placeholder (`idx=90`). Cover (`01`, `21`), section (`03`), ending (`10`), and blank (`17`) layouts suppress page numbers by default.
- If a newly added slide omits its number, enable via `Insert -> Header & Footer -> Slide number`.
- Insert photos and scientific plots through `PICTURE` placeholders and use `Crop` / `Fit` to preserve aspect ratio.

## 4. Standard 21 Layouts Index

| # | Layout Name | Primary Use |
| :--- | :--- | :--- |
| `01` | `01 封面｜研发主题` | Standard R&D report cover |
| `02` | `02 目录｜研究路径` | Agenda / research roadmap (4 items) |
| `03` | `03 章节｜技术坐标` | Section divider |
| `04` | `04 正文｜自由科研画布` | Assertion-evidence layout (title conclusion + visual + interpretation) |
| `05` | `05 对比｜技术方案评审` | Baseline vs candidate design review table |
| `06` | `06 架构｜分层系统数据流` | Context -> Task Intelligence -> Execution & Feedback architecture |
| `07` | `07 实验｜定量证据` | Quantitative plot + KPI callout (`+25 pp` slot) + mechanism note |
| `08` | `08 工程｜现场记录` | Field / sea-trial photo + structured test metadata |
| `09` | `09 计划｜多泳道路线图` | Multi-workstream milestone timeline (`P1`–`P4`) & stage gates |
| `10` | `10 结束｜总结与决策` | Summary, next steps, and decision items |
| `11` | `11 专业｜软件产品矩阵` | Software product matrix & shared technology foundation |
| `12` | `12 专业｜神经网络架构` | Encoder -> Latent transition -> Decoder pipeline |
| `13` | `13 专业｜流场预测与误差` | 12-slot ground truth / prediction / error grid across timesteps |
| `14` | `14 专业｜机器人系统分解` | Robot architecture diagram + subsystem interface specs |
| `15` | `15 专业｜知识产权与成果` | Patents, papers, and software copyrights portfolio |
| `16` | `16 专业｜技术成熟度与验收` | TRL 1–9 scale + verification matrix table |
| `17` | `17 空白｜完全自由画布` | Pure blank canvas |
| `18` | `18 科研｜全幅图证据` | Full-width scientific figure + caption |
| `19` | `19 科研｜双图对比` | Side-by-side two-figure comparison |
| `20` | `20 科研｜四图对比` | 2×2 four-panel condition / temporal comparison |
| `21` | `21 封面｜设备与科研影像` | Cover with real hardware / sea-trial photograph slot |

## 5. Scientific & Engineering Evidence Standards

- State one clear conclusion in each slide title (`Assertion-Evidence` principle).
- Label physical quantities, units, operating conditions, error metrics/bars, and data sources on every plot.
- Clearly distinguish **illustrative diagrams** (`示意`) from **measured field/experimental results** (`实测`), and never represent generic component icons as actual delivered hardware.
