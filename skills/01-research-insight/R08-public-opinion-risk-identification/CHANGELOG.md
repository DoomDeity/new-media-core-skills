# 舆情风险识别（public-opinion-risk-identification）版本记录

> 当前版本：1.0.0（2026-07-23 经项目所有者确认正式定稿）
> 源文件：`skills/01-research-insight/R08-public-opinion-risk-identification/public-opinion-risk-identification.md`

## 1.0.0 — 2026-07-23

经项目所有者确认正式定稿（对应项目进度 v0.23.0）。

- 开发期：R08 自初始草稿经多轮修订达 0.3.0（详见项目 `progress/CHANGELOG.md` v0.11.0–v0.22.0：拆分议题类型与潜在后果严重程度、证据状态针对具体主张、硬性同源去重、与 R07 双向边界、传播风险与业务影响分离、具体主张证据状态合法取值固定为已证实 / 部分证实 / 未证实 / 无法判断、判断置信度须明对象、"无法判断（研判状态，非风险等级）"规则、"待观察"仅作后续监测状态、TWELFTH 轮 T33 语义校正）。十类测试全部通过、待项目所有者确认。
- 定稿：依据 design-spec B7「测试通过、可标完成时升 1.0.0」，版本由开发期 0.3.0 升 1.0.0。
- 补齐定稿辅助文件（README、使用示例、版本记录、发布文案、Agent 兼容运行包），示例全部使用虚构 / 泛化内容，不扩大职责边界。
- 生成 Agent 标准兼容运行包 `dist/standard/public-opinion-risk-identification/SKILL.md`（frontmatter 仅保留 name / description / agent_created，正文由开发源文件自动生成，剔除作者内部自检小节）。

注：本轮仅为定稿、文档补齐与发布包生成，不修改核心业务逻辑，不自动升大版本；定稿后职责 / 工作流重大变化才升大版本。
