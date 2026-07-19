#!/usr/bin/env python3
"""Generate the public catalog from the authoritative skill inventory.

docs/skill-inventory.md is the single source of truth. This script emits:
  - catalog/skills.json   (machine-readable index)
  - catalog/SKILLS.md     (human-readable index)

Run after any change to skill status so the catalog never drifts from the
inventory.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INV = os.path.join(ROOT, "docs", "skill-inventory.md")
CATALOG_DIR = os.path.join(ROOT, "catalog")

CATEGORY_PREFIX = {
    "R": "01-research-insight",
    "C": "02-content-strategy",
    "P": "03-platform-community",
    "G": "04-growth-conversion",
    "D": "05-data-analysis",
    "M": "06-execution-management",
}
CATEGORY_NAME = {
    "01-research-insight": "研究洞察 Research",
    "02-content-strategy": "内容策略与生产 Content",
    "03-platform-community": "平台与社区运营 Platform",
    "04-growth-conversion": "增长与转化 Growth",
    "05-data-analysis": "数据分析与优化 Data",
    "06-execution-management": "项目执行管理 Management",
}

ROW_RE = re.compile(r"^\|\s*(R|C|P|G|D|M)\d{2}\s*\|")


def parse_inventory():
    items = []
    if not os.path.isfile(INV):
        raise SystemExit(f"inventory not found: {INV}")
    for line in open(INV, encoding="utf-8"):
        if not ROW_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        sid, name_zh, name, duty, status, version, test = cells[:7]
        prefix = sid[0]
        category = CATEGORY_PREFIX[prefix]
        source_path = f"skills/{category}/{sid}-{name}/{name}.md"
        dist_path = f"skills/{category}/{sid}-{name}/dist/standard/{name}/SKILL.md"
        published = status == "已定稿"
        test_status = "通过" if published else "未测试"
        items.append({
            "id": sid,
            "name_zh": name_zh,
            "name": name,
            "category": category,
            "version": version if version != "-" else "",
            "status": status,
            "source_path": source_path,
            "dist_path": dist_path,
            "test_status": test_status,
            "published": published,
        })
    return items


def render_skills_md(items):
    out = ["# Skill 目录 / Catalog", ""]
    out.append("> 本文件由 `scripts/generate_catalog.py` 从 `docs/skill-inventory.md` 生成，请勿手改。")
    out.append("> Generated from the authoritative inventory; do not edit by hand.")
    out.append("")
    out.append(f"共 **{len(items)}** 个 Skill，已公开 **{sum(1 for i in items if i['published'])}** 个。")
    out.append("")
    by_cat = {}
    for it in items:
        by_cat.setdefault(it["category"], []).append(it)
    for cat in ["01-research-insight", "02-content-strategy", "03-platform-community",
                "04-growth-conversion", "05-data-analysis", "06-execution-management"]:
        if cat not in by_cat:
            continue
        out.append(f"## {CATEGORY_NAME[cat]}（{cat}）")
        out.append("")
        out.append("| 编号 | 中文名 | 英文名 | 版本 | 状态 | 源文件 | 标准运行包 | 测试 | 已公开 |")
        out.append("|------|--------|--------|------|------|--------|------------|------|--------|")
        for it in by_cat[cat]:
            link_src = "../" + it["source_path"]
            link_dist = "../" + it["dist_path"]
            src = f"[source]({link_src})" if os.path.isfile(os.path.join(ROOT, it["source_path"])) else f"`{it['source_path']}`"
            dist = f"[dist]({link_dist})" if os.path.isfile(os.path.join(ROOT, it["dist_path"])) else f"`{it['dist_path']}`"
            ver = it["version"] or "-"
            out.append(f"| {it['id']} | {it['name_zh']} | {it['name']} | {ver} | {it['status']} | {src} | {dist} | {it['test_status']} | {'是' if it['published'] else '否'} |")
        out.append("")
    return "\n".join(out) + "\n"


def main():
    items = parse_inventory()
    os.makedirs(CATALOG_DIR, exist_ok=True)
    with open(os.path.join(CATALOG_DIR, "skills.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    with open(os.path.join(CATALOG_DIR, "SKILLS.md"), "w", encoding="utf-8") as f:
        f.write(render_skills_md(items))
    print(f"generate_catalog: wrote {len(items)} skills to catalog/skills.json and catalog/SKILLS.md")


if __name__ == "__main__":
    main()
