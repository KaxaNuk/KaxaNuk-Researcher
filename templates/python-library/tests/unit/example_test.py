"""
Tests of `percentage_change`: the change it returns, and the error it raises from zero.
"""
import pytest

import kn_python_library_template


@pytest.mark.parametrize(
    (
        'start',
        'end',
        'expected',
    ),
    [
        (
            100.0,
            110.0,
            0.1,
        ),
        (
            50.0,
            25.0,
            -0.5,
        ),
    ],
)
def test_percentage_change(
    start: float,
    end: float,
    expected: float,
) -> None:
    """
    A rise and a fall, each as a fraction of the start.
    """
    change = kn_python_library_template.percentage_change(
        start,
        end,
    )

    assert change == pytest.approx(expected)


def test_percentage_change_from_zero() -> None:
    """
    A start of zero raises the library's own error, which a caller can catch.
    """
    with pytest.raises(
        kn_python_library_template.KnPythonLibraryTemplateError,
    ):
        kn_python_library_template.percentage_change(
            0.0,
            1.0,
        )
