from pathlib import Path
import ast

queue = Path("queue")
projects = sorted(queue.glob("[0-9][0-9][0-9]_*"))
assert len(projects) == 100, f"Expected 100 projects, found {len(projects)}"

for p in projects:
    source = p / "lambda_function.py"
    ast.parse(source.read_text())
    assert (p/"README.md").exists()
    assert (p/"requirements.txt").exists()
    assert (p/"test_event.json").exists()

print("Validated 100 project folders and Python syntax.")
