#!/usr/bin/env python3
from pathlib import Path
import re
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: python scripts/update_progress.py <project-folder>")

project = sys.argv[1]
readme = Path("README.md")

if not readme.exists():
    raise SystemExit("README.md not found")

match = re.match(r"^(\d+)_", project)
if not match:
    raise SystemExit(f"Invalid project folder name: {project}")

day = int(match.group(1))
text = readme.read_text(encoding="utf-8")

# Match:
# | 1 | `001_hello_world` | ... | ⏳ |
pattern = re.compile(
    rf"^(\|\s*{day}\s*\|\s*`{re.escape(project)}`\s*\|[^|\n]+\|\s*)(?:⏳|🔄|✅)(\s*\|.*)$",
    re.MULTILINE,
)

new_text, count = pattern.subn(r"\1✅\2", text, count=1)

if count == 0:
    raise SystemExit(f"Progress marker not found for Day {day}: {project}")

readme.write_text(new_text, encoding="utf-8")
print(f"Updated README: Day {day} ({project}) -> ✅")
