# Skill 清单（50 个）

> 状态：已确认。本文件为 50 个核心 Skill 的唯一权威清单。编号、名称、分类、职责边界与开发顺序以本文件为准，不得自行增删改。
> 最近更新：2026-07-23

## 编号与命名规则

- 编号：R/C/P/G/D/M + 两位数（仅项目索引用，只放在 Skill 目录名中，不写入源文件名与 frontmatter 的 `name`）。
  - Research：R01–R08｜Content：C01–C15｜Platform：P01–P05｜Growth：G01–G09｜Data：D01–D07｜Management：M01–M06
- 英文目录名：小写 kebab-case，与中文名一一对应。
- 源路径：`skills/<分类目录>/<编号>-<英文目录名>/`，开发源文件命名：`<英文目录名>.md`（如 `industry-research.md`，编号只放目录名 `R01-industry-research/`），每个目录仅一份，不使用 `SKILL.md` 作为开发源文件名。
  - 分类目录：01-research-insight / 02-content-strategy / 03-platform-community / 04-growth-conversion / 05-data-analysis / 06-execution-management
- 状态：未开始 / 草稿 / 待测试 / 已完成。版本：语义化，初始 0.1.0。
- 测试记录路径：`tests/<编号>-<英文目录名>/test-record.md`。

## 01 Research Skills｜研究洞察，共 8 个

| 编号 | 名称 | 英文目录名 | 一句话职责 | 状态 | 版本 | 测试记录 |
|------|------|-----------|-----------|------|------|---------|
| R01 | 行业研究 | industry-research | 研究行业结构、趋势、竞争与机会。 | 已定稿 | 1.3.0 | tests/R01-industry-research/test-record.md |
| R02 | 竞品定位分析 | competitor-positioning-analysis | 分析竞品用户、需求、价值主张与定位。 | 已定稿 | 1.3.0 | tests/R02-competitor-positioning-analysis/test-record.md |
| R03 | 竞品内容分析 | competitor-content-analysis | 分析竞品内容方向、栏目、形式与表现。 | 已定稿 | 1.3.0 | tests/R03-competitor-content-analysis/test-record.md |
| R04 | 竞品营销策略拆解 | competitor-marketing-strategy-analysis | 拆解竞品传播、获客、承接和转化路径。 | 已定稿 | 1.3.0 | tests/R04-competitor-marketing-strategy-analysis/test-record.md |
| R05 | 用户评论分析 | user-comment-analysis | 从评论反馈中提取问题、需求与情绪。 | 已定稿 | 1.3.0 | tests/R05-user-comment-analysis/test-record.md |
| R06 | 用户需求挖掘 | user-needs-discovery | 识别显性需求、隐性需求及优先级。 | 已定稿 | 1.0.0 | tests/R06-user-needs-discovery/test-record.md |
| R07 | 热点趋势监测 | trend-monitoring | 监测并判断行业、平台和社会趋势。 | 已定稿 | 1.0.0 | tests/R07-trend-monitoring/test-record.md |
| R08 | 舆情风险识别 | public-opinion-risk-identification | 识别负面舆情、争议和升级风险。 | 已定稿 | 1.0.0 | tests/R08-public-opinion-risk-identification/test-record.md |

## 02 Content Skills｜内容策略与生产，共 15 个

| 编号 | 名称 | 英文目录名 | 一句话职责 | 状态 | 版本 | 测试记录 |
|------|------|-----------|-----------|------|------|---------|
| C01 | 账号定位分析 | account-positioning-analysis | 设计或诊断账号的目标用户与价值定位。 | 未开始 | - | - |
| C02 | 内容栏目规划 | content-pillar-planning | 建立稳定、可持续的内容栏目体系。 | 未开始 | - | - |
| C03 | 月度内容规划 | monthly-content-planning | 制定月度选题、栏目和发布安排。 | 未开始 | - | - |
| C04 | 选题生成 | topic-generation | 根据用户、平台和业务目标生成选题。 | 未开始 | - | - |
| C05 | 选题价值评分 | topic-value-scoring | 评价选题的流量、价值、转化和成本。 | 未开始 | - | - |
| C06 | 短视频口播稿 | short-video-talking-script | 生成自然、可拍摄、时长可控的口播稿。 | 未开始 | - | - |
| C07 | 短视频分镜脚本 | short-video-storyboard | 将内容转化为镜头、画面和节奏安排。 | 未开始 | - | - |
| C08 | 小红书图文 | xiaohongshu-post | 生成适配小红书语境的完整图文内容。 | 未开始 | - | - |
| C09 | 营销文案 | marketing-copywriting | 生成用于品牌、产品、活动和转化的文案。 | 未开始 | - | - |
| C10 | 标题生成 | title-generation | 根据平台、用户和内容生成标题。 | 未开始 | - | - |
| C11 | 一稿多平台改编 | cross-platform-content-adaptation | 将同一内容适配为不同平台版本。 | 未开始 | - | - |
| C12 | 中英文内容本地化 | bilingual-content-localization | 根据文化和用户习惯进行中英文本地化。 | 未开始 | - | - |
| C13 | 内容质量评分 | content-quality-assessment | 按统一标准评价内容并提出修改建议。 | 未开始 | - | - |
| C14 | 品牌口径检查 | brand-message-consistency-check | 检查事实、术语、卖点和定位的一致性。 | 未开始 | - | - |
| C15 | 平台违规风险检查 | platform-compliance-risk-check | 识别内容的违规、敏感与合规风险。 | 未开始 | - | - |

## 03 Platform Skills｜平台与社区运营，共 5 个

| 编号 | 名称 | 英文目录名 | 一句话职责 | 状态 | 版本 | 测试记录 |
|------|------|-----------|-----------|------|------|---------|
| P01 | 账号诊断 | account-diagnosis | 根据主页、内容和数据诊断账号问题。 | 未开始 | - | - |
| P02 | 多平台发布排期 | multi-platform-publishing-schedule | 制定多平台发布节奏和排期。 | 未开始 | - | - |
| P03 | 评论区回复 | comment-reply | 识别评论意图并生成公开回复。 | 未开始 | - | - |
| P04 | 负面评论处理 | negative-comment-handling | 分类负面评论并制定处理方案。 | 未开始 | - | - |
| P05 | 平台规则监测 | platform-rule-monitoring | 追踪平台规则、功能和机制变化。 | 未开始 | - | - |

## 04 Growth Skills｜增长与转化，共 9 个

| 编号 | 名称 | 英文目录名 | 一句话职责 | 状态 | 版本 | 测试记录 |
|------|------|-----------|-----------|------|------|---------|
| G01 | 内容获客路径 | content-acquisition-path | 设计内容曝光到线索或成交的路径。 | 未开始 | - | - |
| G02 | 转化漏斗诊断 | conversion-funnel-diagnosis | 定位转化环节中的流失和障碍。 | 未开始 | - | - |
| G03 | 落地页诊断 | landing-page-diagnosis | 诊断落地页价值、信任、结构与CTA。 | 未开始 | - | - |
| G04 | 销售话术 | sales-talk-track | 根据产品、客户和阶段生成销售话术。 | 未开始 | - | - |
| G05 | 客户异议处理 | customer-objection-handling | 针对价格、效果和信任等异议设计回应。 | 未开始 | - | - |
| G06 | 体验转付费流程 | trial-to-paid-conversion | 设计从体验到正式付费的完整流程。 | 未开始 | - | - |
| G07 | 私域承接流程 | private-domain-conversion-flow | 设计公域用户进入私域后的承接转化。 | 未开始 | - | - |
| G08 | 达人筛选 | creator-selection | 根据产品、人群、内容和数据筛选达人。 | 未开始 | - | - |
| G09 | 达人邀约 | creator-outreach | 生成针对不同达人的个性化邀约。 | 未开始 | - | - |

## 05 Data Skills｜数据分析与优化，共 7 个

| 编号 | 名称 | 英文目录名 | 一句话职责 | 状态 | 版本 | 测试记录 |
|------|------|-----------|-----------|------|------|---------|
| D01 | KPI设计 | kpi-design | 将业务目标拆解为可监控指标。 | 未开始 | - | - |
| D02 | 数据看板规划 | dashboard-planning | 设计看板指标、维度、口径和层级。 | 未开始 | - | - |
| D03 | 内容表现分析 | content-performance-analysis | 分析内容曝光、观看、互动和转化表现。 | 未开始 | - | - |
| D04 | 用户行为分析 | user-behavior-analysis | 分析用户路径、行为变化和异常点。 | 未开始 | - | - |
| D05 | ROI分析 | roi-analysis | 分析内容、渠道、活动或项目投入产出。 | 未开始 | - | - |
| D06 | A/B测试分析 | ab-test-analysis | 分析实验差异并提出下一步决策。 | 未开始 | - | - |
| D07 | 数据周报 | weekly-data-report | 将周度数据转化为结论与行动建议。 | 未开始 | - | - |

## 06 Management Skills｜项目执行管理，共 6 个

| 编号 | 名称 | 英文目录名 | 一句话职责 | 状态 | 版本 | 测试记录 |
|------|------|-----------|-----------|------|------|---------|
| M01 | 项目任务拆解 | project-task-breakdown | 将目标拆解为任务、交付物与完成标准。 | 未开始 | - | - |
| M02 | 项目计划生成 | project-plan-generation | 制定阶段、里程碑、时间和依赖关系。 | 未开始 | - | - |
| M03 | 项目风险识别 | project-risk-identification | 识别目标、资源、进度和质量风险。 | 未开始 | - | - |
| M04 | 会议纪要转任务 | meeting-notes-to-actions | 从会议内容提取结论、任务和待确认项。 | 未开始 | - | - |
| M05 | SOP生成 | sop-generation | 将成熟做法整理为可执行标准流程。 | 未开始 | - | - |
| M06 | 管理层汇报 | executive-reporting | 提炼结果、问题、风险和决策事项。 | 未开始 | - | - |
