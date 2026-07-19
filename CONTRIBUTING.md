# 贡献指南 / Contributing

本仓库收录一套固定的 50 个新媒体核心 Skill。贡献聚焦于把这 50 个 Skill 高质量地做完，而不是自由新增。

## 基本原则

1. **一个 Skill 只承担一个独立任务。** 不拆分已有职责，也不把多个任务塞进一个 Skill。
2. **不擅自增删合并既定 50 个 Skill。** 清单以 `docs/skill-inventory.md` 为唯一权威，新增/删除需先对齐项目所有者。
3. **新 Skill 必须符合目录与命名规则。** 目录 `<编号>-<skill-name>/`，源文件 `<skill-name>.md`，编号只放目录名，`name` 与目录、源文件名一致（详见 `docs/design-spec.md` B1）。
4. **新 Skill 必须先经过测试。** 按 `docs/test-spec.md` 完成十类测试并记录到 `tests/<编号>-<skill-name>/test-record.md`，未通过不得标完成。
5. **定稿辅助文件只在确认定稿后生成。** README、CHANGELOG、examples、publish、dist 仅在项目所有者明确"定稿"后补齐。
6. **不提交真实隐私数据。** 评论、私信、用户样本必须先匿名化；不提交含姓名、手机号、账号的原始材料。
7. **不提交密钥。** 不提交 API Key、Token、Cookie、`.env` 或任何凭证。
8. **不直接修改 dist 中的 `SKILL.md`。** 运行包由 `scripts/build_dist.py` 从源文件生成；改源文件后重新构建。
9. **修改源文件后必须重新构建 dist。** 运行 `python scripts/build_dist.py` 并保持 `git diff` 为空。
10. **PR 必须通过自动校验。** `validate-skills.yml` 失败时先本地运行 `python scripts/validate_repository.py` 修复。

## 提交流程

1. 从 `main` 切出分支。
2. 按 `templates/` 与 `docs/skill-quality-playbook.md` 开发/修订。
3. 运行 `python scripts/validate_repository.py`，确保无错误。
4. 运行 `python scripts/build_dist.py`，确保 dist 与源文件一致。
5. 运行 `python scripts/generate_catalog.py`，更新公开索引。
6. 提交 PR，描述改动与测试结果。

## 创建前 / 创建后检查

使用 `templates/skill-review-checklist.md` 完成创建前与创建后检查，避免重复已确认的错误做法。
