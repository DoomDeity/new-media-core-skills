#!/usr/bin/env python3
"""Build standard Agent dist packages from skill source files.

Scans skills/<category>/<id>-<name>/<name>.md and generates
skills/<category>/<id>-<name>/dist/standard/<name>/SKILL.md with a
trimmed, compatibility-verified frontmatter and an identical body.

The development source file is the single source of truth. This script
never edits it. Runtime-needed references/scripts/assets are copied into
the dist package when present.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")

# frontmatter fields confirmed supported by skill-creator / standard agents
KEEP_FIELDS = ("name", "description", "agent_created")

CATEGORY_PREFIX = {
    "R": "01-research-insight",
    "C": "02-content-strategy",
    "P": "03-platform-community",
    "G": "04-growth-conversion",
    "D": "05-data-analysis",
    "M": "06-execution-management",
}

SKILL_DIR_RE = re.compile(r"^(R|C|P|G|D|M)\d{2}-(.+)$")


def find_skill_dirs():
    dirs = []
    if not os.path.isdir(SKILLS_DIR):
        return dirs
    for cat in sorted(os.listdir(SKILLS_DIR)):
        cat_path = os.path.join(SKILLS_DIR, cat)
        if not os.path.isdir(cat_path):
            continue
        for entry in sorted(os.listdir(cat_path)):
            if not SKILL_DIR_RE.match(entry):
                continue
            d = os.path.join(cat_path, entry)
            if os.path.isdir(d):
                dirs.append(d)
    return dirs


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


def build_one(skill_dir, check=False):
    errors = []
    base = os.path.basename(os.path.normpath(skill_dir))
    m = SKILL_DIR_RE.match(base)
    if not m:
        return [f"{skill_dir}: not a valid skill dir"]
    prefix, name = m.group(1), m.group(2)
    src = os.path.join(skill_dir, f"{name}.md")
    if not os.path.isfile(src):
        return [f"{skill_dir}: source file {name}.md not found"]
    text = open(src, encoding="utf-8").read()
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as e:
        return [f"{skill_dir}: {e}"]
    if fields.get("name") != name:
        errors.append(f"{skill_dir}: frontmatter name '{fields.get('name')}' != '{name}'")
    if "description" not in fields:
        errors.append(f"{skill_dir}: missing description")
    new_fm = (
        f"---\nname: {fields['name']}\n"
        f"description: {fields['description']}\n"
        f"agent_created: true\n---\n"
    )
    content = new_fm + body
    out_dir = os.path.join(skill_dir, "dist", "standard", name)
    out_path = os.path.join(out_dir, "SKILL.md")
    if check:
        if not os.path.exists(out_path):
            errors.append(f"{skill_dir}: dist SKILL.md missing (run build_dist.py)")
        elif open(out_path, encoding="utf-8").read() != content:
            errors.append(f"{skill_dir}: dist SKILL.md differs from source (run build_dist.py)")
        return errors
    os.makedirs(out_dir, exist_ok=True)
    for sub in ("references", "scripts", "assets"):
        src_sub = os.path.join(skill_dir, sub)
        if os.path.isdir(src_sub) and os.listdir(src_sub):
            dest_sub = os.path.join(out_dir, sub)
            os.makedirs(dest_sub, exist_ok=True)
            for item in sorted(os.listdir(src_sub)):
                s = os.path.join(src_sub, item)
                d = os.path.join(dest_sub, item)
                if os.path.isfile(s):
                    with open(s, "rb") as fi, open(d, "wb") as fo:
                        fo.write(fi.read())
    with open(out_path, "w", encoding="utf-8", newline="\n") as fo:
        fo.write(content)
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", help="specific skill dir under skills/ (e.g. skills/01-research-insight/R01-industry-research)")
    ap.add_argument("--check", action="store_true", help="check only, do not write")
    args = ap.parse_args()
    if args.skill:
        d = args.skill if os.path.isabs(args.skill) else os.path.join(ROOT, args.skill)
        if not os.path.isdir(d):
            print(f"ERROR: skill dir not found: {d}", file=sys.stderr)
            sys.exit(2)
        dirs = [d]
    else:
        dirs = find_skill_dirs()
    all_errors = []
    for d in dirs:
        errs = build_one(d, check=args.check)
        all_errors.extend(errs)
        if not errs:
            print(f"OK {os.path.relpath(d, ROOT)}")
    if all_errors:
        print("\nERRORS:", file=sys.stderr)
        for e in all_errors:
            print(" - " + e, file=sys.stderr)
        sys.exit(1)
    print("build_dist: all dist packages consistent.")


if __name__ == "__main__":
    main()
