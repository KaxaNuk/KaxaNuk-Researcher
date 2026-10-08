"""
The library's errors.

Every error the library raises derives from `KnPythonLibraryTemplateError`, so a
caller catches them all with a single `except` clause.
"""
__all__ = [
    'KnPythonLibraryTemplateError',
]


class KnPythonLibraryTemplateError(Exception):
    """
    An error a caller can handle: input the library cannot use, a file it cannot find.
    """
