<!--
Skill 开发源文件模板（仅结构 + 检查提示，不预填业务答案）。
用法：复制为 skills/<分类>/<编号>-<skill-name>/<skill-name>.md，按注释填写。
编号只放目录名；源文件名与 frontmatter 的 name 都等于 <skill-name>。
完整质量规则见 docs/skill-quality-playbook.md 与 docs/design-spec.md。
-->
---
name: <skill-name>          # 小写 kebab-case；与目录编号后的英文名、源文件名一致；不含编号
description: <What this skill does, and when to use it. 第三人称，明确"做什么 + 什么情况下使用"。>
agent_created: true
version: 0.1.0              # 可选；初始 0.1.0，定稿 1.x.0
updated: YYYY-MM-DD         # 可选
---

# <中文名>

## When to Use
<!-- 列出 3+ 典型触发场景与用户说法。只覆盖本 Skill 唯一职责。 -->

## When NOT to Use
<!-- 列出禁止触发场景，并引用相邻 Skill（如"只分析单竞品定位 → 用 competitor-positioning-analysis"）。避免误触发与职责重叠。 -->

## Inputs
<!-- 声明必要输入；缺失且可合理假设时标"假设：…"继续；缺失会实质影响结果时集中询问一次。 -->

## 缺失信息处理
<!-- 明确：可假设什么、必须问什么、绝不静默编造什么。 -->

## Workflow
<!-- 命令式步骤。最后一步放自检：有无无来源数字？推断是否冒充事实？维度是否混淆？示例是否自洽？ -->

## Output
<!-- 默认 Markdown。说明输出结构与落盘路径（如有）。输出应可直接使用。 -->

## Evidence / Quality Rules
<!-- 统一前缀：事实 / 推断 / 未知 / 建议。不把推断或假设写成事实；不编造数据；小样本用实际数量而非精确百分比。 -->

## Boundaries
<!-- 能力边界、不做什么、隐私与外部工具边界。涉及用户材料时写明先匿名化、不提交外部搜索/第三方工具。 -->

## Examples
<!-- 1–2 个精炼示例，全部虚构/脱敏；不复制某具体 Skill 的业务逻辑。 -->

## 最终自检
<!-- 发布前逐项核对：触发准确、边界清晰、无来源数字、推断已标注、示例自洽、未写死工具、未越界。 -->
