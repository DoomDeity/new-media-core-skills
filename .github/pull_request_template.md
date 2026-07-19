## 改动说明

- 关联 Skill / 编号：
- 改动类型：新增 / 修订 / 文档 / 脚本
- 测试结果（如涉及 Skill 改动）：

## 检查清单

- [ ] 已运行 `python scripts/validate_repository.py` 并通过
- [ ] 已运行 `python scripts/build_dist.py`，dist 与源文件一致（无 git diff）
- [ ] 已运行 `python scripts/generate_catalog.py`（如 Skill 状态变化）
- [ ] 未提交密钥、本地路径或隐私数据
- [ ] 不擅自增删既定 50 个 Skill
- [ ] 定稿辅助文件仅在确认定稿后生成
- [ ] 修改只改开发源文件，未直接改 `dist/` 中的 `SKILL.md`
