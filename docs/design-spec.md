# Skill 设计规范

> 状态：A 部分（已核实事实）+ B1–B9（本项目已落地规范）。本文件供 50 个 Skill 开发与校验统一遵循。
> 最近更新：2026-07-19

## A. 环境中已验证的事实（已核实，非猜测）

以下来自当前 WorkBuddy 环境中真实存在的 skill-creator 指南、官方初始化脚本及已安装 Skill 实例：

1. **运行时/兼容包格式（已核实）**：WorkBuddy 运行时与标准技能包中，每个 Skill 目录必须包含 `SKILL.md`，加载位置见 A9。本项目人工维护的开发源文件不使用 `SKILL.md` 命名，改用 `<skill-name>.md`，且编号只放在目录名中（见 B10）。可选资源目录为 `scripts/`（可执行脚本）、`references/`（按需加载的参考文档）、`assets/`（用于输出的模板/素材）。
2. **frontmatter 必填字段**：`name`、`description`。`description` 决定触发时机，需具体说明"做什么 + 何时使用"。
3. **frontmatter 强制字段（校验器要求）**：`agent_created: true`——skill-creator 校验流程要求该字段，供 skill_manage 后续修改/删除。
4. **frontmatter 常见可选字段**（真实实例中出现，非强制）：`version`、`author`、`created`、`updated`、`license`、`allowed-tools`、`display_name`、`description_zh`/`description_en`、`visibility`。
5. **三级渐进加载**：元数据（name+description，约 100 词，常驻上下文）→ SKILL.md 正文（触发后加载，建议 <5000 词）→ 捆绑资源（按需加载，无上限）。正文保持精简，长篇资料放 `references/`。
6. **写作风格**：正文使用命令式/动词开头的祈使句，面向另一个 AI 实例书写。
7. **正文结构参考**（真实实例）：`## When to Use` / `## When NOT to Use` 分节明确触发与禁止触发条件——与本项目"触发准确、边界清晰"的目标一致。
8. **官方工具脚本**（位于 skill-creator 内）：
   - 初始化：`scripts/init_skill.py <skill-name> --path <目录>`
   - 校验：`scripts/quick_validate.py`
   - 打包：`scripts/package_skill.py <skill目录>`（打包前自动校验 frontmatter、命名、目录结构）
9. **加载位置（当前环境已核实）**：用户级 `~/.workbuddy/skills/<skill-name>/`；项目级 `<项目根>/.workbuddy/skills/<skill-name>/`（扁平结构，不含分类目录）。
   - **历史兼容**：早期 CodeBuddy 文档曾写作 `~/.codebuddy/skills/` 与 `.codebuddy/skills/`，属遗留命名，当前环境不再使用，标记为历史兼容、不再采用。
   - 从源目录 `skills/<分类>/<编号>-<skill-name>/<skill-name>.md` 到加载目录的同步方式见 B8（待验证）。

## B. 本项目规范（已落地）

### B1 命名规则
- 编号：R/C/P/G/D/M + 两位数（R01–R08、C01–C15、P01–P05、G01–G09、D01–D07、M01–M06），仅用于项目索引与进度追踪，**只放在 Skill 目录名称中，不写入源文件名与 frontmatter 的 `name`**。
- Skill 目录名：`<编号>-<英文Skill名>`（小写 kebab-case，与中文名一一对应），存放于 `skills/<分类目录>/<编号>-<英文Skill名>/`。
- 源文件名：`<英文Skill名>.md`（仅含 name，不含编号），与 frontmatter 的 `name` 及目录中编号后的英文名完全一致。
- 分类目录：01-research-insight / 02-content-strategy / 03-platform-community / 04-growth-conversion / 05-data-analysis / 06-execution-management。
- 每个 Skill 目录只保留一份开发源文件，不使用 `SKILL.md` 作为开发源文件名。
- 中文名、英文 Skill 名、编号的对应关系以 `docs/skill-inventory.md` 为唯一清单，不得自行增删改。

### B2 frontmatter 统一字段
- **必填（校验器强制）**：`name`、`description`、`agent_created: true`。
- **可选（非校验器强制，按项目需要）**：`version`（语义化，初始 0.1.0，用于变更追踪）、`updated`（最后更新日期，YYYY-MM-DD）、`author`（可选）。
- 不加入校验器未声明或当前环境未证实的字段；未知字段标记为"待验证"。
- `description` 写法见 B4。

### B3 SKILL.md 正文章节模板
统一章节（空章节可省略，但 When to Use 与 When NOT to Use 必须存在）：
1. **When to Use** — 触发场景与典型用户说法。
2. **When NOT to Use** — 禁止触发场景，并与相邻 Skill 互相引用边界。
3. **Inputs** — 必要输入信息，及缺失处理口径。
4. **Workflow** — 执行步骤，命令式。
5. **Output** — 输出物格式与落盘路径。
6. **Boundaries** — 能力边界、不做什么、事实/推断/假设标注。
7. **Examples** — 1–2 个精炼示例。
- 正文控制在 5000 词以内；长方法、框架、字段字典放 `references/`。

### B4 触发与边界写法
- `description` 用第三人称，明确"做什么 + 什么情况下使用"。示例：
  "This skill should be used when the user wants to analyze a competitor's positioning, including target users, needs, value proposition, and differentiation."
- When NOT to Use 必须列出相邻 Skill，避免误触发与职责重叠。
- 同一请求可能命中的相邻 Skill，在双方 When NOT to Use 中互相引用。

### B5 输入输出规范
- **输入**：在 Inputs 中声明必要信息；缺失且可合理假设时，标注"假设：…"后继续；缺失会实质影响结果时，集中询问一次（仅问关键项，不逐条追问）。
- **输出**：默认 Markdown；需落盘的文件使用绝对路径（或项目根内相对路径）；不虚构数据、来源、平台规则或用户资料。

### B6 事实 / 推断 / 假设标注
正文用统一前缀区分：
- **事实**：已核实的信息。
- **推断**：基于已知信息的合理推论。
- **假设**：为继续推进而暂定的前提。
- **待验证**：环境或外部未证实的事项。
- **建议**：可选行动。
不把推断或假设写成事实。

### B7 版本规则
- 初始 `0.1.0`（起草）；修订升 `0.x`；测试通过、可标完成时升 `1.0.0`。
- 每次实质修改同步更新项目版本记录（内部进度）与 `docs/skill-inventory.md` 的版本字段。

### B8 部署同步方式（待验证）
- 开发源（唯一人工维护）：`skills/<分类>/<编号>-<skill-name>/<skill-name>.md`。
- 加载（已核实）：用户级 `~/.workbuddy/skills/<skill-name>/`、项目级 `<根>/.workbuddy/skills/<skill-name>/`（扁平，标准包含 `SKILL.md`）。
- 兼容包生成：Skill 定稿后，由开发源文件自动复制/转换为标准包 `SKILL.md`（置于临时或发布目录）；该 `SKILL.md` 非人工维护第二份，修改须回到开发源文件重新生成。
- 同步/打包方式（复制到加载目录、zip 打包等）：当前环境未实测，标记为"待验证"；正式部署前须以实际验证结果为准，不在开发阶段执行。

### B9 单 Skill 资源边界
- `references/`：仅当存在长方法、框架、字段字典、示例库等需按需加载的内容时创建；>10k 词时给出 grep 检索模式。
- `scripts/`：仅当需确定性脚本（如解析、计算）且会反复重写时创建。
- `assets/`：仅当输出需要模板/图片/样板文件时创建。
- 不为了"完整"而堆砌 resources；开发源文件与兼容包 `SKILL.md` 均保持精简，不机械复制统一模板。

### B10 开发源文件与兼容运行包

- 开发源文件 `<skill-name>.md`（位于 `skills/<分类>/<编号>-<skill-name>/`）是本项目唯一人工维护的 Skill 正文文件；后续修改只改该文件。
- WorkBuddy 能直接导入开发源文件时直接使用，无需改名。
- 当外部工具（如 Codex）或标准技能包结构要求 `SKILL.md` 时，在 Skill 定稿后自动生成兼容包；兼容包 `SKILL.md` 由开发源文件复制/转换生成，不作为第二份人工维护源文件。
- 兼容包如需修改，必须先改开发源文件再重新生成；不允许同时维护开发源文件与 `SKILL.md` 两套正文。
- skill-creator 校验只接受 `SKILL.md` 时，可在临时/发布目录生成标准入口文件校验，不改变开发源文件命名。
- 部署/加载目录与同步方式见 B8（待验证）。

### B11 定稿生命周期（已落地）

Skill 从开发到发布的统一生命周期，覆盖开发、测试、定稿、辅助文件、发布资料、兼容包与一致性校验：

1. 开发阶段只维护带英文名称的唯一源文件（`<skill-name>.md`），不强求发布辅助文件。
2. 编号只放在 Skill 目录名称中，不放在源文件名和 frontmatter 的 `name` 中。
3. 只有项目所有者明确说"定稿""通过""可以发布"或同等含义时，Skill 才进入定稿阶段；未经确认，WorkBuddy 不得自行宣布定稿。
4. 生命周期顺序：开发源文件 → 测试与修订 → 项目所有者确认定稿 → 补齐人类阅读文件（README / 示例 / 版本记录）→ 生成平台发布资料（publish/）→ 生成 Agent 兼容运行包（dist/standard/<skill-name>/SKILL.md）→ 最终一致性校验。
5. 定稿后按需补齐：README、使用示例、版本记录、平台发布文案、Agent 兼容运行包，以及实际需要的 references / scripts / assets；不得为了形式完整创建无内容、无用途的文件和目录。
6. Agent 兼容包中的 `SKILL.md` 是自动生成的发布产物，不是人工维护源文件；后续修改必须先改源文件再重生成，不得直接改 `SKILL.md` 造成分叉。
7. 兼容包 frontmatter 只允许保留目标 Agent 已确认支持的字段（本环境已验证：`name`、`description`；skill-creator 校验强制 `agent_created: true`）；`version`、`updated` 等项目管理信息保留在源文件、README 与 CHANGELOG，不强制写入运行包。
8. 运行包内不包含 README、项目测试记录、项目进度或内部 CHANGELOG；只包含运行时真正需要的文件；references / scripts / assets 仅在运行时需要时才复制进入运行包。
9. 定稿辅助文件完成后，必须执行源文件、README、示例、发布资料与运行包的一致性检查（见 test-spec 一致性条款）。
10. 后续 50 个 Skill 全部遵循本规则。

### B12 复盘沉淀的永久创建规则（已落地）

基于 R01–R05 多轮返工，新增以下强约束（详细经验见 `docs/skill-quality-playbook.md`，检查清单见 `templates/skill-review-checklist.md`）：

1. 创建任何新 Skill 前，先读取 `docs/skill-inventory.md`、`docs/skill-quality-playbook.md`、`templates/skill-review-checklist.md` 与当前 Skill 的相邻 Skill 文件。
2. 生成初稿前完成"创建前检查"：唯一职责、相邻 Skill、绝对不触发的请求、输入是否真实可获得、是否需要联网/文件/用户样本、适合该任务的证据来源、隐私与合规风险、是否需要 references / scripts / assets。
3. 生成后完成"创建后检查"：description 边界是否清晰、Workflow 是否真实可执行、是否存在无来源数字、是否存在推断冒充事实、是否存在伪精确、示例是否虚构且自洽、是否写死具体工具、是否越过 Skill 边界、是否与相邻 Skill 重复、是否考虑缺失输入、是否完成实际测试、是否仍处于开发阶段、是否错误地提前创建发布文件。
4. 后续 Skill 第一次交付应直接满足 R01–R05 最终定稿形成的质量要求，不得重复已确认错误的旧做法。
5. 不得为套模板而降低不同 Skill 的专业差异；模板只约束结构、证据、边界与质量，不替代具体业务设计。
6. 新 Skill 完成实际测试后，才允许提交项目所有者审查。
7. 项目所有者确认定稿后，才生成 README、CHANGELOG、examples、publish 与 dist。
8. R01–R05 作为已通过的参考实现，其业务逻辑不得复制到不相关 Skill。
