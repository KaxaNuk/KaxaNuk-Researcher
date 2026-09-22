"""
Pytest configuration: make the skill scripts importable as plain modules.
"""
import pathlib
import sys

CONFTEST_PATH = pathlib.Path(__file__)
REPOSITORY_ROOT = CONFTEST_PATH.resolve().parent.parent
SKILL_SCRIPT_DIRECTORIES = [
    REPOSITORY_ROOT / '.apm' / 'skills' / 'bloom-code-lint' / 'scripts',
    REPOSITORY_ROOT / '.apm' / 'skills' / 'init-strategy' / 'scripts',
    REPOSITORY_ROOT / '.apm' / 'skills' / 'propagate-mcp-env-vars' / 'scripts',
    REPOSITORY_ROOT / '.apm' / 'skills' / 'read' / 'scripts',
    REPOSITORY_ROOT / 'tools',
]

for script_directory in SKILL_SCRIPT_DIRECTORIES:
    directory_string = str(script_directory)
    sys.path.insert(
        0,
        directory_string,
    )
