# 发布指南 / Publishing Guide

本文件说明一个 Skill 从"已定稿"到对外发布的标准动作与边界。核心是：**定稿前不发布，发布前必过校验与隐私检查。**

## 1. 发布前提

只有满足以下条件才能发布：

1. 项目所有者明确确认"定稿"。
2. 十类测试（研究型至少九类）全部通过，记录于 `tests/<编号>-<skill-name>/test-record.md`。
3. 已补齐 README、CHANGELOG、examples、publish 与 dist（见 design-spec B11）。
4. 通过 `python scripts/validate_repository.py`。
5. 通过隐私与密钥审计（无任何未脱敏个人数据、无密钥）。

## 2. 发布到本 GitHub 仓库

- 本仓库为公开仓库；提交即公开。
- 提交前确认 `.gitignore` 已排除 `.workbuddy/`、`progress/`、`.env`、未脱敏测试数据。
- 提交信息建议：`feat: finalize <id> <name>`。
- 不得 force push，不得重写已公开历史。

## 3. 发布到 RedSkill / 小红书

- `publish/redskill.md` 是发布准备文案，**不是** RedSkill 官方 Manifest，也不假设任何固定平台目录格式。
- 实际上传前必须核实平台当时的上传方式与要求，本文件不替代平台规则。
- 不声称获得官方认证、官方推荐或平台背书。
- 不把"分析"宣传为"保证结果"；不使用夸张、无法证明的效果承诺。
- 涉及评论、用户反馈或平台数据时，发布文案必须保留隐私与合规提醒。

## 4. 部署到 WorkBuddy / Codex

- 部署同步方式当前为"待验证"（见 design-spec B8），正式部署前以目标环境实际验证结果为准。
- 修改 Skill 后必须先改开发源文件，再运行 `python scripts/build_dist.py` 重新生成运行包，不得直接改 `dist/` 中的 `SKILL.md`。

## 5. 发布前检查清单

- [ ] 开发源文件、README、CHANGELOG、examples、publish、dist 均已补齐且版本一致
- [ ] `python scripts/build_dist.py` 重新生成 dist，无差异
- [ ] `python scripts/validate_repository.py` 通过
- [ ] `python scripts/generate_catalog.py` 已更新公开索引
- [ ] 无本地绝对路径、用户名、密钥、手机号等泄露
- [ ] 评论/用户样本已匿名化
- [ ] 发布文案无夸大承诺、无官方认证声明
- [ ] 许可证状态已在 README 中正确说明
