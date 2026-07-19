# 新媒体核心 Skill 系统 / New Media Core Skills

> 面向新媒体研究、内容、平台运营、增长转化、数据分析和项目管理的 Agent Skill 集合。
> A production-ready collection of 50 agent skills for new media research, content, growth, data analysis, and operations.

**当前进度：5 / 50 已定稿。** 本仓库是一个长期维护的公开单体仓库，未来将持续收录剩余 45 个 Skill。

- 英文简介：A production-ready collection of 50 agent skills for new media research, content, growth, data analysis, and operations.
- 兼容环境：WorkBuddy、Codex 及其他支持 Markdown 或标准 Skill 目录的 Agent。

---

## 项目目标

完成并维护 **50 个**新媒体核心 Agent Skill，覆盖 6 大类，作为可复用、可测试、可审计的能力模块。每个 Skill 从开发源文件出发，经测试、定稿、补齐人类阅读文件、生成发布资料与 Agent 兼容运行包。

## 当前进度

| 指标 | 值 |
|------|-----|
| 计划总数 | 50 |
| 已定稿 | 5 |
| 已公开 | 5 |
| 规划中 | 45 |

## 六大分类

| 编号 | 分类 | 目录 | 数量 | 状态 |
|------|------|------|------|------|
| 01 | 研究洞察 | `skills/01-research-insight/` | 8 | R01–R05 已定稿 |
| 02 | 内容策略与生产 | `skills/02-content-strategy/` | 15 | 规划中 |
| 03 | 平台与社区运营 | `skills/03-platform-community/` | 5 | 规划中 |
| 04 | 增长与转化 | `skills/04-growth-conversion/` | 9 | 规划中 |
| 05 | 数据分析与优化 | `skills/05-data-analysis/` | 7 | 规划中 |
| 06 | 项目执行管理 | `skills/06-execution-management/` | 6 | 规划中 |

## 已发布 Skill

| 编号 | 中文名 | 英文名 | 版本 | 状态 | 源文件 | 标准运行包 |
|------|--------|--------|------|------|--------|------------|
| R01 | 行业研究 | industry-research | 1.3.0 | 已定稿 | [source](skills/01-research-insight/R01-industry-research/industry-research.md) | [dist](skills/01-research-insight/R01-industry-research/dist/standard/industry-research/SKILL.md) |
| R02 | 竞品定位分析 | competitor-positioning-analysis | 1.3.0 | 已定稿 | [source](skills/01-research-insight/R02-competitor-positioning-analysis/competitor-positioning-analysis.md) | [dist](skills/01-research-insight/R02-competitor-positioning-analysis/dist/standard/competitor-positioning-analysis/SKILL.md) |
| R03 | 竞品内容分析 | competitor-content-analysis | 1.3.0 | 已定稿 | [source](skills/01-research-insight/R03-competitor-content-analysis/competitor-content-analysis.md) | [dist](skills/01-research-insight/R03-competitor-content-analysis/dist/standard/competitor-content-analysis/SKILL.md) |
| R04 | 竞品营销策略拆解 | competitor-marketing-strategy-analysis | 1.3.0 | 已定稿 | [source](skills/01-research-insight/R04-competitor-marketing-strategy-analysis/competitor-marketing-strategy-analysis.md) | [dist](skills/01-research-insight/R04-competitor-marketing-strategy-analysis/dist/standard/competitor-marketing-strategy-analysis/SKILL.md) |
| R05 | 用户评论分析 | user-comment-analysis | 1.3.0 | 已定稿 | [source](skills/01-research-insight/R05-user-comment-analysis/user-comment-analysis.md) | [dist](skills/01-research-insight/R05-user-comment-analysis/dist/standard/user-comment-analysis/SKILL.md) |

> 其余 45 个 Skill 在 `docs/skill-inventory.md` 与 `catalog/SKILLS.md` 中显示为规划状态，尚未创建空目录或占位文件。

## Skill 源文件 vs 标准运行包

- **开发源文件** `skills/<分类>/<编号>-<skill-name>/<skill-name>.md`：唯一人工维护的 Skill 正文，编号只放在目录名中。
- **标准运行包** `skills/<分类>/<编号>-<skill-name>/dist/standard/<skill-name>/SKILL.md`：由源文件自动生成，供要求 `SKILL.md` 的 Agent 使用，不属于第二份人工维护源文件。

修改 Skill 时只改源文件，再运行 `scripts/build_dist.py` 重新生成运行包。

## 如何使用

### WorkBuddy

WorkBuddy 可直接使用带英文名称的 Markdown 源文件。具体导入方式以 WorkBuddy 当前版本为准；本项目开发源文件可通过 WorkBuddy 的 Skill 加载机制使用。

### Codex 及通用 Agent

使用每个 Skill 的标准运行包：`skills/<分类>/<编号>-<skill-name>/dist/standard/<skill-name>/SKILL.md`。不同 Agent 对 frontmatter 与辅助文件的支持可能不同，未验证的平台标记为"待验证"。

## 仓库目录

```
new-media-core-skills/
├── README.md                     # 本文件
├── CHANGELOG.md                  # 仓库级版本记录
├── CONTRIBUTING.md               # 贡献规范
├── .gitignore
├── .github/                     # Workflow 与 Issue/PR 模板
├── catalog/                     # 公开索引（SKILLS.md + skills.json）
├── docs/                        # 设计规范、测试规范、兼容/发布/质量文档
├── templates/                   # 新 Skill 模板与检查清单
├── scripts/                     # 校验与构建脚本
├── skills/                      # 各 Skill（源文件 + 辅助文件 + 运行包）
└── tests/                       # 脱敏后的公开测试记录
```

## 如何查找合适的 Skill

1. 先读 `docs/skill-inventory.md`（50 个 Skill 的权威清单）。
2. 按六大分类进入 `skills/<分类>/` 目录。
3. 阅读目标 Skill 的 `README.md` 判断适用/不适用场景。
4. 参考 `examples/EXAMPLES.md` 确认触发与边界。

## 质量标准

每个 Skill 必须：可独立调用、触发准确、边界清晰、输出可用、不编造事实。详见 `docs/test-spec.md`（十类测试）与 `docs/skill-quality-playbook.md`（复盘沉淀的质量规则）。

## 测试说明

每个 Skill 需通过十类测试（研究型至少九类），记录于 `tests/<编号>-<skill-name>/test-record.md`。未通过不得标记为完成。

## 兼容性说明

详见 `docs/compatibility.md`。本仓库的兼容声明基于真实验证；未验证的平台标记为"待验证"。**本仓库未获得 WorkBuddy、OpenAI、Codex 或 RedSkill 官方认证。**

## 后续路线图

- R06–R08（研究洞察剩余 3 个）进入开发。
- 按 `docs/skill-inventory.md` 顺序、每批 ≤5 个推进，直至 50 个全部定稿。

## 贡献方式

见 `CONTRIBUTING.md`。新 Skill 必须符合目录与命名规则、先经测试、定稿辅助文件仅在确认定稿后生成；修改源文件后必须重新构建 dist 并通过自动校验。

## 许可证状态

**当前仓库尚未授予开源许可证。** 公开可见不代表允许复制、修改、再分发或商业使用。许可证将在后续由项目所有者决定；在此之前请勿将本仓库内容用于上述用途。

## 不夸大兼容范围

本仓库不声称所有 Agent 无需调整即可运行，也不声称获得任何平台官方认证。具体导入方式以目标平台当前规则为准。
