"""
The template's example: one public function, tested in `tests/unit/example_test.py`.

Replace this file and its test with the library's first module and its test, and its line in
`__init__.py` with the new module's.
"""
__all__ = [
    'percentage_change',
]

from kn_python_library_template.exceptions import (
    KnPythonLibraryTemplateError,
)


def percentage_change(
    start: float,
    end: float,
) -> float:
    """
    The change from `start` to `end` as a fraction of `start`: 0.1 from 100 to 110.

    Raises `KnPythonLibraryTemplateError` when `start` is zero,
    since a change from zero has no size.
    """
    if start == 0:
        message = 'start is zero, and a change from zero has no size'

        raise KnPythonLibraryTemplateError(message)

    change = (end - start) / start

    return change
