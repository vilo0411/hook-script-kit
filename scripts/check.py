#!/usr/bin/env python3
"""Check local Markdown links and skill portability, using Python stdlib only."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def check(root):
    root = root.resolve()
    errors = []
    docs = sorted(root.rglob("*.md"))
    for doc in docs:
        source = doc.read_text(encoding="utf-8")
        # This toolkit uses inline Markdown links, without spaces in filenames.
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", source):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            dest = (doc.parent / unquote(url.path)).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"{doc.relative_to(root)}: missing/outside link {target}")
    skill = root / "skills/hook-script/SKILL.md"
    if not skill.exists():
        skill = root / "SKILL.md"  # Also accept a copied, standalone skill.
    if not skill.exists():
        errors.append("Missing SKILL.md")
    else:
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append("Skill needs YAML frontmatter")
        else:
            fields = dict(re.findall(r"^(name|description):\s*(.+)$", match[1], re.M))
            if fields.get("name") != "hook-script" or not fields.get("description"):
                errors.append("Skill name/description is invalid")
    return docs, errors


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    docs, errors = check(root)
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(docs)} Markdown files; {len(errors)} errors.")
    sys.exit(bool(errors))
