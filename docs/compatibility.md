# 兼容性说明 / Compatibility

本文件说明 `new-media-core-skills` 如何与不同 Agent 环境协作，以及哪些声明已验证、哪些待验证。

## 1. WorkBuddy

- WorkBuddy 可直接使用带英文名称的 Markdown 开发源文件（`skills/<分类>/<编号>-<skill-name>/<skill-name>.md`）。
- 具体导入/启用方式以 WorkBuddy 当前版本为准；本项目不假定任何固定菜单或命令。
- 兼容包 `SKILL.md` 仅在需要标准 Skill 目录结构时由 `scripts/build_dist.py` 生成。

## 2. Codex 及采用标准 Skill 目录的 Agent

- 优先使用每个 Skill 的标准运行包：`skills/<分类>/<编号>-<skill-name>/dist/standard/<skill-name>/SKILL.md`。
- 该 `SKILL.md` 由开发源文件自动生成，frontmatter 仅保留已验证字段 `name` / `description` / `agent_created: true`。
- `version`、`updated` 等项目管理信息保留在源文件、README 与 CHANGELOG 中，不强制写入运行包。

## 3. 不同 Agent 的差异

- 不同 Agent 对 frontmatter 字段、辅助文件（`references/`、`scripts/`、`assets/`）和触发机制的支持可能不同。
- 本仓库不保证所有 Agent 无需调整即可运行。
- 若某 Agent 需要扩展字段（如 `allowed-tools`、`display_name`），应在该 Agent 的兼容层处理，不污染开发源文件。

## 4. 兼容声明的边界

- 所有兼容声明必须基于真实验证（见各 Skill 的测试记录与 `scripts/validate_repository.py`）。
- 未经验证的平台一律标记为"待验证"，不假设其支持。
- **本仓库未获得 WorkBuddy、OpenAI、Codex 或 RedSkill 官方认证。** 任何"官方推荐/认证"的说法均不成立。

## 5. 当前已验证 / 待验证

| 项目 | 状态 |
|------|------|
| 开发源文件结构（name / 目录 / frontmatter 一致） | 已验证 |
| `dist/standard/<name>/SKILL.md` 由源文件生成且正文一致 | 已验证（build_dist.py） |
| `quick_validate.py`（skill-creator）对运行包校验通过 | 已验证（R01–R05） |
| `agents/openai.yaml` 标准清单 | 待验证（规范未确认，未生成） |
| WorkBuddy / Codex 实际部署同步方式 | 待验证（见 design-spec B8） |
| RedSkill / 小红书实际上传格式 | 待验证（发布前以平台规则为准） |
