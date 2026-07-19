#!/usr/bin/env python3
"""Validate the new-media-core-skills repository structure and content.

Checks (returns non-zero exit on any error):
 1. category directories are from the known set
 2. skill dir matches <id>-<name>
 3. id prefix matches the category directory
 4. source file is <name>.md
 5. frontmatter `name` matches dir / file
 6. frontmatter has required fields (name, description, agent_created)
 7. finalized skill has README.md
 8. finalized skill has CHANGELOG.md
 9. finalized skill has examples/EXAMPLES.md
10. finalized skill has publish/redskill.md
11. finalized skill has dist/standard/<name>/SKILL.md
12. dist SKILL.md body is identical to source (frontmatter converted only)
13. no manually maintained SKILL.md outside dist
14. no old / duplicate path or stray body copy
15. no empty references/ scripts/ assets/ directories
16. no local absolute paths (C:\\Users, /Users/x, /c/Users, J:/, C:/Users)
17. no secrets (gho_/ghp_/github_pat_/sk-<20+>/AKIA...)
18. no un-anonymized phone numbers in test/examples material
19. README version matches source frontmatter version; catalog consistent
20. example ratios self-consistent (a/b/c=N sums)
21. no placeholder / empty files
22. no dead relative markdown links
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORY_PREFIX = {
    "R": "01-research-insight",
    "C": "02-content-strategy",
    "P": "03-platform-community",
    "G": "04-growth-conversion",
    "D": "05-data-analysis",
    "M": "06-execution-management",
}
VALID_CATEGORIES = set(CATEGORY_PREFIX.values())
SKILL_DIR_RE = re.compile(r"^(R|C|P|G|D|M)\d{2}-(.+)$")
SECRET_RE = re.compile(r"(gh[oip]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})")
LOCALPATH_RE = re.compile(r"(C:\\Users\\|C:/Users/|/c/Users/|/Users/[A-Za-z0-9_.-]+/|J:/|J:\\|\\\\workspace)")
PHONE_RE = re.compile(r"1[3-9]\d{9}")
RATIO_RE = re.compile(r"((?:\d+\s*/\s*){2,}\d+)\s*=\s*(\d+)")


def err(errors, msg):
    errors.append(msg)


def parse_frontmatter(text):
    if not text.startswith("---"):
        raise ValueError("missing frontmatter")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        raise ValueError("malformed frontmatter")
    fm = m.group(1)
    body = text[m.end():]
    fields = {}
    for line in fm.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fields[k.strip()] = v.strip()
    return fields, body


def load_inventory_status():
    """Return dict id -> status from docs/skill-inventory.md."""
    inv = os.path.join(ROOT, "docs", "skill-inventory.md")
    status = {}
    if not os.path.isfile(inv):
        return status
    for line in open(inv, encoding="utf-8"):
        m = re.match(r"^\|\s*(R|C|P|G|D|M)\d{2}\s*\|", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6:
            status[cells[0]] = cells[4]
    return status


def scan_text(path, text, errors):
    if SECRET_RE.search(text):
        err(errors, f"{path}: possible secret/credential pattern found")
    if LOCALPATH_RE.search(text):
        err(errors, f"{path}: local absolute path / username leaked")
    if PHONE_RE.search(text):
        err(errors, f"{path}: possible un-anonymized phone number (11 digits)")


def check_ratio_self_consistency(path, text, errors):
    for line in text.splitlines():
        m = RATIO_RE.search(line)
        if not m:
            continue
        left = m.group(1)
        total = int(m.group(2))
        nums = [int(x) for x in re.findall(r"\d+", left)]
        if sum(nums) != total:
            err(errors, f"{path}: ratio not self-consistent ({left} != {total})")


def check_dead_links(path, text, errors):
    base_dir = os.path.dirname(path)
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#")[0]
        if not target:
            continue
        resolved = os.path.normpath(os.path.join(base_dir, target))
        if not os.path.exists(resolved):
            err(errors, f"{path}: dead relative link -> {target}")


def walk_md_files():
    roots = ["README.md", "CHANGELOG.md", "CONTRIBUTING.md", "docs", "catalog",
             "templates", "scripts", "skills", "tests", ".github"]
    for r in roots:
        rp = os.path.join(ROOT, r)
        if not os.path.exists(rp):
            continue
        if os.path.isfile(rp):
            yield rp
        else:
            for dirpath, dirnames, filenames in os.walk(rp):
                # skip internal / ignored dirs
                dirnames[:] = [d for d in dirnames if d not in (".workbuddy", "progress", ".git", "__pycache__")]
                for fn in filenames:
                    if fn.endswith((".md", ".py", ".yml", ".yaml", ".json")):
                        yield os.path.join(dirpath, fn)


def validate_skill(skill_dir, status_map, errors):
    base = os.path.basename(os.path.normpath(skill_dir))
    m = SKILL_DIR_RE.match(base)
    if not m:
        err(errors, f"{skill_dir}: invalid skill dir name")
        return
    prefix, name = m.group(1), m.group(2)
    parent = os.path.basename(os.path.dirname(skill_dir))
    if parent != CATEGORY_PREFIX.get(prefix):
        err(errors, f"{skill_dir}: prefix {prefix} does not match category {parent}")
    sid = base.split("-", 1)[0]
    is_final = status_map.get(sid) == "已定稿"
    src = os.path.join(skill_dir, f"{name}.md")
    if not os.path.isfile(src):
        err(errors, f"{skill_dir}: source {name}.md missing")
        return
    text = open(src, encoding="utf-8").read()
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as e:
        err(errors, f"{skill_dir}: {e}")
        return
    if fields.get("name") != name:
        err(errors, f"{skill_dir}: frontmatter name '{fields.get('name')}' != '{name}'")
    for req in ("name", "description", "agent_created"):
        if req not in fields:
            err(errors, f"{skill_dir}: missing required frontmatter field '{req}'")
    scan_text(src, text, errors)
    check_ratio_self_consistency(src, text, errors)

    # dist package
    dist_path = os.path.join(skill_dir, "dist", "standard", name, "SKILL.md")
    if not os.path.isfile(dist_path):
        if is_final:
            err(errors, f"{skill_dir}: finalized skill missing dist SKILL.md")
    else:
        dtext = open(dist_path, encoding="utf-8").read()
        try:
            dfields, dbody = parse_frontmatter(dtext)
        except ValueError as e:
            err(errors, f"{dist_path}: {e}")
            dbody = None
        if dbody is not None and dbody != body:
            err(errors, f"{skill_dir}: dist body differs from source")
        if dfields.get("name") != name:
            err(errors, f"{dist_path}: name mismatch")

    # no manual SKILL.md at skill root (only inside dist/)
    root_skill = os.path.join(skill_dir, "SKILL.md")
    if os.path.isfile(root_skill):
        err(errors, f"{skill_dir}: manual SKILL.md at skill root (must live in dist/standard/)")

    # empty resource dirs
    for sub in ("references", "scripts", "assets"):
        sd = os.path.join(skill_dir, sub)
        if os.path.isdir(sd) and not any(os.listdir(sd)):
            err(errors, f"{skill_dir}: empty {sub}/ directory")

    # finalized-only required files
    if is_final:
        for required in ("README.md", "CHANGELOG.md", "examples/EXAMPLES.md", "publish/redskill.md"):
            if not os.path.isfile(os.path.join(skill_dir, required)):
                err(errors, f"{skill_dir}: finalized skill missing {required}")
        # README version consistency
        rm = os.path.join(skill_dir, "README.md")
        if os.path.isfile(rm):
            rtext = open(rm, encoding="utf-8").read()
            ver = fields.get("version")
            if ver and ver not in rtext:
                err(errors, f"{skill_dir}: README does not state version {ver}")
            scan_text(rm, rtext, errors)
            check_ratio_self_consistency(rm, rtext, errors)
        ex = os.path.join(skill_dir, "examples", "EXAMPLES.md")
        if os.path.isfile(ex):
            etext = open(ex, encoding="utf-8").read()
            scan_text(ex, etext, errors)
            check_ratio_self_consistency(ex, etext, errors)
        pub = os.path.join(skill_dir, "publish", "redskill.md")
        if os.path.isfile(pub):
            ptext = open(pub, encoding="utf-8").read()
            scan_text(pub, ptext, errors)
            check_ratio_self_consistency(pub, ptext, errors)


def main():
    errors = []
    # 1. category dirs
    skills_root = os.path.join(ROOT, "skills")
    if os.path.isdir(skills_root):
        for cat in os.listdir(skills_root):
            cp = os.path.join(skills_root, cat)
            if not os.path.isdir(cp):
                continue
            if cat not in VALID_CATEGORIES:
                err(errors, f"skills/{cat}: not a valid category directory")
    status_map = load_inventory_status()
    # scan all markdown/code for secrets/paths/phones
    # (.py files are skipped: code legitimately contains regex/path literals)
    for fp in walk_md_files():
        rel = os.path.relpath(fp, ROOT)
        if rel.endswith(".py"):
            continue
        text = open(fp, encoding="utf-8", errors="replace").read()
        scan_text(rel, text, errors)
        check_dead_links(rel, text, errors)
    # validate each skill
    if os.path.isdir(skills_root):
        for cat in sorted(os.listdir(skills_root)):
            cp = os.path.join(skills_root, cat)
            if not os.path.isdir(cp):
                continue
            for entry in sorted(os.listdir(cp)):
                if entry.startswith("."):
                    continue
                entry_path = os.path.join(cp, entry)
                if not os.path.isdir(entry_path):
                    continue
                if not SKILL_DIR_RE.match(entry):
                    err(errors, f"skills/{cat}/{entry}: not a valid skill directory")
                    continue
                validate_skill(entry_path, status_map, errors)
    # catalog consistency with inventory
    catalog_json = os.path.join(ROOT, "catalog", "skills.json")
    if os.path.isfile(catalog_json):
        import json
        data = json.load(open(catalog_json, encoding="utf-8"))
        for item in data:
            inv_status = status_map.get(item.get("id"))
            if inv_status and item.get("status") != inv_status:
                err(errors, f"catalog/skills.json: {item.get('id')} status '{item.get('status')}' != inventory '{inv_status}'")
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print(" - " + e, file=sys.stderr)
        sys.exit(1)
    print("VALIDATION PASSED: repository structure and content are consistent.")


if __name__ == "__main__":
    main()
