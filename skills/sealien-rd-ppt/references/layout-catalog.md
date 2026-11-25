# Layout & Component Catalog (V4.1.0)

## 1. Slide Layouts (`templates/powerpoint/Sealien_RD_Master_V4.1.0.pptx`)

| Index | Layout Name | Placeholders (`idx: TYPE`) | Best For |
| :--- | :--- | :--- | :--- |
| `01` | `01 封面｜研发主题` | `101:TITLE, 102:BODY, 103:BODY` | Standard cover page |
| `02` | `02 目录｜研究路径` | `101:TITLE, 102..110:BODY, 90:SLIDE_NUMBER` | 4-section agenda & research path |
| `03` | `03 章节｜技术坐标` | `101:BODY, 102:TITLE, 103:BODY` | Section divider |
| `04` | `04 正文｜自由科研画布` | `101:TITLE, 102:BODY, 103:OBJECT, 90:SLIDE_NUMBER` | General assertion-evidence slide |
| `05` | `05 对比｜技术方案评审` | `101:TITLE, 102:BODY, 103:OBJECT, 104:BODY, 90:SLIDE_NUMBER` | Trade-off & design review table |
| `06` | `06 架构｜分层系统数据流` | `101:TITLE, 102:BODY, 103:OBJECT, 90:SLIDE_NUMBER` | Layered architecture & dataflow |
| `07` | `07 实验｜定量证据` | `101:TITLE, 102:BODY, 103:CHART, 104..107:BODY, 90:SLIDE_NUMBER` | Quantitative plot + KPI callout |
| `08` | `08 工程｜现场记录` | `101:TITLE, 102:BODY, 103:PICTURE, 104..108:BODY, 90:SLIDE_NUMBER` | Field / sea-trial photo & test log |
| `09` | `09 计划｜多泳道路线图` | `101:TITLE, 102:BODY, 103:OBJECT, 104:BODY, 90:SLIDE_NUMBER` | Workstream roadmap & stage gates |
| `10` | `10 结束｜总结与决策` | `101:TITLE, 102:BODY, 103:BODY` | Summary & action decisions |
| `11` | `11 专业｜软件产品矩阵` | `101:TITLE, 102..112:BODY, 90:SLIDE_NUMBER` | Software ecosystem & shared platform |
| `12` | `12 专业｜神经网络架构` | `101:TITLE, 102:BODY, 103:OBJECT, 104..106:BODY, 90:SLIDE_NUMBER` | Encoder-latent-decoder network diagram |
| `13` | `13 专业｜流场预测与误差` | `101:TITLE, 102:BODY, 103..114:PICTURE (12), 115..116:BODY, 90:SLIDE_NUMBER` | GT / Pred / Error spatiotemporal grid |
| `14` | `14 专业｜机器人系统分解` | `101:TITLE, 102:BODY, 103:PICTURE, 104..108:BODY, 90:SLIDE_NUMBER` | Hardware/CAD + interface spec list |
| `15` | `15 专业｜知识产权与成果` | `101:TITLE, 102..114:BODY, 90:SLIDE_NUMBER` | Patents, papers, software copyrights |
| `16` | `16 专业｜技术成熟度与验收` | `101:TITLE, 102..103:BODY, 104:TABLE, 105:BODY, 90:SLIDE_NUMBER` | TRL 1–9 assessment & acceptance table |
| `17` | `17 空白｜完全自由画布` | *(none)* | Unconstrained custom canvas |
| `18` | `18 科研｜全幅图证据` | `101:TITLE, 102:BODY, 103:PICTURE, 104:BODY, 90:SLIDE_NUMBER` | Full-width single scientific figure |
| `19` | `19 科研｜双图对比` | `101:TITLE, 102:BODY, 103..104:PICTURE, 105..108:BODY, 90:SLIDE_NUMBER` | Two-figure side-by-side comparison |
| `20` | `20 科研｜四图对比` | `101:TITLE, 102:BODY, 103..106:PICTURE, 107..110:BODY, 90:SLIDE_NUMBER` | 2×2 four-panel condition grid |
| `21` | `21 封面｜设备与科研影像` | `101:TITLE, 102:BODY, 103:BODY, 104:PICTURE` | Photo-backed equipment/trial cover |

## 2. Editable Component Groups (`components/Sealien_RD_Components_V4.1.0.pptx`)

- **Page 1 (`architecture/`)**: `01 输入节点`, `02 处理模块`, `03 数据存储`, `04 外部接口`, `05 反馈闭环`, `06 安全决策`
- **Page 2 (`architecture/`)**: `07 张量特征栈`, `08 编码—解码`, `09 时序序列`, `10 潜空间节点`, `11 双分支网络`, `12 状态机`
- **Page 3 (`scientific-visualization/`)**: `13 指标与单位`, `14 趋势曲线示意`, `15 对比柱示意`, `16 误差棒示意`, `17 图像标注`, `18 多图编号`
- **Page 4 (`robotics/`)**: `19 传感器`, `20 推进器`, `21 作业机构`, `22 设备边界`, `23 接口标注`, `24 局部放大`
- **Page 5 (`project-management/`)**: `25 阶段门`, `26 计划条`, `27 需求—证据`, `28 风险项`, `29 验收状态`, `30 版本与交付`
- **Page 6 (`project-management/`)**: `31 章节编号`, `32 核心结论`, `33 流程步骤`, `34 文档证据`, `35 技术标签`, `36 引用与来源`
- **Page 7 (`architecture/`)**: `37 API 服务`, `38 消息队列`, `39 容器与部署`, `40 状态快照`, `41 原子发布`, `42 权限与安全边界`
- **Page 8 (`scientific-visualization/`)**: `43 仿真网格`, `44 真值与预测`, `45 误差色标`, `46 消融对比`, `47 收敛曲线`, `48 多步预测`
- **Page 9 (`robotics/`)**: `49 声呐扫描`, `50 AUV 侧视`, `51 ROV 框架`, `52 坐标系与方向`, `53 流速与扰动`, `54 多机协同`
- **Page 10 (`project-management/`)**: `55 需求追踪`, `56 测试用例`, `57 验收证据`, `58 TRL 等级`, `59 风险矩阵`, `60 行动与责任`
