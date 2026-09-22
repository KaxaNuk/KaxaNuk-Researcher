"""
Copy a KaxaNuk starting point into a new folder: a researcher's home, a strategy, or the example.

The three starting points ship inside the KaxaNuk Researcher package — `templates/researcher/`,
`templates/strategy/` and `examples/liquid-golden-cross/` — and this script copies one of them
byte for byte, so every folder made from the same package version starts identical.  Nothing is
written from memory and nothing is generated.

Usage:
    uv run --no-project python scaffold.py researcher <destination>
    uv run --no-project python scaffold.py strategy <destination>
    uv run --no-project python scaffold.py example <destination>
    uv run --no-project python scaffold.py example <strategy root> --only Experiments/Experiment_1

Without `--only`, the destination must not exist or must be an empty folder; the copy is then made
a git repository on branch `main` with one first commit, unless `--no-git`.  With `--only`, one
path of the starting point is copied into an existing folder: a file already there with the same
content is skipped, and one with other content stops the run before anything is written, so
nothing is overwritten.

The package is found beside this script when it runs from a checkout of KaxaNuk-Researcher, then
under `apm_modules/` in the folder it runs from or any folder above it, then under `~/.apm/`, where
`apm install -g` puts it.  `--package` names it outright.

Exit code 0 when the copy was made, 1 when nothing was written.  Console output is ASCII only.
"""
import argparse
import dataclasses
import pathlib
import shutil
import subprocess
import sys

# Each starting point: where it sits inside the package, and the first commit of a copy of it.
STARTING_POINTS = {
    'researcher': (
        'templates/researcher',
        'Start from the KaxaNuk Researcher template',
    ),
    'strategy': (
        'templates/strategy',
        'Start from the KaxaNuk Strategy Template',
    ),
    'example': (
        'examples/liquid-golden-cross',
        'Start from the KaxaNuk example strategy, liquid-golden-cross',
    ),
}
# Where APM puts the package, relative to an `apm_modules/` folder: from GitHub, then from a path.
INSTALLED_PACKAGE_PATHS = [
    pathlib.Path('KaxaNuk') / 'KaxaNuk-Researcher',
    pathlib.Path('_local') / 'KaxaNuk-Researcher',
]
# The package root seen from this file: scripts/ -> init-strategy/ -> skills/ -> .apm/ -> the root.
SCRIPT_PATH = pathlib.Path(__file__).resolve()
SOURCE_PACKAGE = SCRIPT_PATH.parents[4]
USER_SCOPE_MODULES = pathlib.Path.home() / '.apm' / 'apm_modules'
MISSING_PACKAGE = ' '.join([
    'The researcher package was not found. Install it with',
    '`apm install -g KaxaNuk/KaxaNuk-Researcher --target <agent>`, or pass --package.',
])


@dataclasses.dataclass(frozen=True)
class CopyPlan:
    """
    What one run copies: every source file and the path it lands at.
    """
    source_root: pathlib.Path
    destination_root: pathlib.Path
    files: tuple[tuple[pathlib.Path, pathlib.Path], ...]


def copy_files(
    plan: CopyPlan,
) -> None:
    """
    Copy every file in the plan, creating the folders it needs.
    """
    for source, target in plan.files:
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        shutil.copy2(
            source,
            target,
        )


def find_package(
    explicit: pathlib.Path | None,
    start: pathlib.Path,
) -> pathlib.Path | None:
    """
    The KaxaNuk Researcher package's root: the one given, the checkout this script sits in, or an install.
    """
    if explicit is not None:
        given = explicit if _is_package(explicit) else None

        return given

    candidates = [
        SOURCE_PACKAGE,
        *_installed_candidates(start),
    ]
    packages = [
        candidate
        for candidate
        in candidates
        if _is_package(candidate)
    ]
    found = packages[0] if packages else None

    return found


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Parse the command line, check the destination, copy, and make the copy a git repository.
    """
    parser = _build_parser()
    parsed = parser.parse_args(arguments)
    package = find_package(
        parsed.package,
        pathlib.Path.cwd(),
    )

    if package is None:
        print(MISSING_PACKAGE)

        return 1

    relative_source, first_commit = STARTING_POINTS[parsed.kind]
    source_root = package / relative_source
    destination = parsed.destination.resolve()

    if parsed.only is not None:
        exit_code = _copy_one_path(
            source_root,
            destination,
            parsed.only,
        )

        return exit_code

    problem = _destination_problem(destination)

    if problem is not None:
        print(problem)

        return 1

    plan = plan_copy(
        source_root,
        destination,
    )
    copy_files(plan)
    print(f'Copied {len(plan.files)} files from {source_root} to {destination}')

    if not parsed.no_git:
        _make_repository(
            destination,
            first_commit,
        )

    return 0


def plan_copy(
    source_root: pathlib.Path,
    destination_root: pathlib.Path,
) -> CopyPlan:
    """
    Every file under the source, in a stable order, paired with the path it lands at.
    """
    sources = sorted(
        path
        for path
        in source_root.rglob('*')
        if path.is_file()
    )
    files = tuple(
        (
            source,
            destination_root / source.relative_to(source_root),
        )
        for source
        in sources
    )
    plan = CopyPlan(
        source_root=source_root,
        destination_root=destination_root,
        files=files,
    )

    return plan


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: which starting point, where to, and the three options.
    """
    parser = argparse.ArgumentParser(
        description='Copy a KaxaNuk starting point into a new folder.',
    )
    parser.add_argument(
        'kind',
        choices=sorted(STARTING_POINTS),
        help='researcher, strategy or example',
    )
    parser.add_argument(
        'destination',
        type=pathlib.Path,
        help='the new folder; with --only, the existing folder to copy into',
    )
    parser.add_argument(
        '--only',
        type=pathlib.PurePosixPath,
        default=None,
        help='copy one file or folder of the starting point into an existing folder',
    )
    parser.add_argument(
        '--no-git',
        action='store_true',
        help='leave the copy as plain files, with no git repository',
    )
    parser.add_argument(
        '--package',
        type=pathlib.Path,
        default=None,
        help='the researcher package folder, when it cannot be found on its own',
    )

    return parser


def _copy_one_path(
    source_root: pathlib.Path,
    destination: pathlib.Path,
    only: pathlib.PurePosixPath,
) -> int:
    """
    Copy one file or folder of the starting point into an existing folder, overwriting nothing.
    """
    source = source_root / only
    target = destination / only

    if not destination.is_dir():
        print(f'{destination} is not an existing folder; --only copies into one')

        return 1

    if not source.exists():
        print(f'{only} is not part of this starting point')

        return 1

    if source.is_file():
        plan = CopyPlan(
            source_root=source.parent,
            destination_root=target.parent,
            files=((source, target),),
        )
    else:
        plan = plan_copy(
            source,
            target,
        )

    different = [
        str(landing.relative_to(destination))
        for origin, landing
        in plan.files
        if _differs(
            origin,
            landing,
        )
    ]

    if different:
        print('Nothing was copied; these files already exist with other content:')

        for path in different:
            print(f'  {path}')

        return 1

    missing = tuple(
        (origin, landing)
        for origin, landing
        in plan.files
        if not landing.exists()
    )
    missing_plan = CopyPlan(
        source_root=plan.source_root,
        destination_root=plan.destination_root,
        files=missing,
    )
    copy_files(missing_plan)
    already_there = len(plan.files) - len(missing)
    print(f'Copied {len(missing)} files into {target}; {already_there} were already there, identical')

    return 0


def _destination_problem(
    destination: pathlib.Path,
) -> str | None:
    """
    Why the destination cannot take a new copy, or None when it can.
    """
    if not destination.exists():

        return None

    if not destination.is_dir():
        not_a_folder = f'{destination} exists and is not a folder'

        return not_a_folder

    contents = list(destination.iterdir())

    if contents:
        not_empty = f'{destination} is not empty; choose a new folder'

        return not_empty

    return None


def _differs(
    origin: pathlib.Path,
    landing: pathlib.Path,
) -> bool:
    """
    Whether a file already sits where a copy would land, with content other than the copy's.
    """
    if not landing.exists():

        return False

    same = landing.read_bytes() == origin.read_bytes()

    return not same


def _installed_candidates(
    start: pathlib.Path,
) -> list[pathlib.Path]:
    """
    Where an install may have put the package: in `apm_modules/` at or above `start`, then at user scope.
    """
    module_folders = [
        folder / 'apm_modules'
        for folder
        in [start.resolve(), *start.resolve().parents]
    ]
    module_folders.append(USER_SCOPE_MODULES)
    candidates = [
        modules / package_path
        for modules
        in module_folders
        for package_path
        in INSTALLED_PACKAGE_PATHS
    ]

    return candidates


def _is_package(
    candidate: pathlib.Path,
) -> bool:
    """
    Whether a folder holds the three starting points.
    """
    holds_all = all(
        (candidate / relative_source).is_dir()
        for relative_source, _
        in STARTING_POINTS.values()
    )

    return holds_all


def _make_repository(
    destination: pathlib.Path,
    first_commit: str,
) -> None:
    """
    Make the copy a git repository on branch `main` with one first commit, and say so.

    A failed step is reported; a failed commit also with the command that finishes it.
    """
    commands = [
        [
            'git',
            'init',
            '--quiet',
            '--initial-branch=main',
        ],
        [
            'git',
            'add',
            '--all',
        ],
        [
            'git',
            'commit',
            '--quiet',
            '-m',
            first_commit,
        ],
    ]

    for command in commands:
        completed = subprocess.run(
            command,
            cwd=destination,
            capture_output=True,
            text=True,
            check=False,
        )

        if completed.returncode != 0:
            print(f'`{" ".join(command[:2])}` failed; the files are copied, the repository is not finished:')
            print(completed.stderr.strip())

            if command[1] == 'commit':
                print(f'Finish it in that folder with: git commit -m "{first_commit}"')

            return

    print(f'Made it a git repository, first commit: "{first_commit}"')


if __name__ == '__main__':
    sys.exit(main())
