"""
Sphinx's settings for the library's documentation.

Read the Docs builds it from `.readthedocs.yml`, and
`uv run sphinx-build -W -b html docs/source docs/_build/html` builds it here.
"""
import kn_python_library_template

# The project, as every page names it, and its version, read from the package.
project = 'KN Python Library Template'
release = kn_python_library_template.__version__

# Pages in Markdown through MyST, and the API from the docstrings: written in prose, read by
# napoleon when they hold numpy-style sections, a single backtick setting code.
default_role = 'literal'
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
]
napoleon_google_docstring = False
napoleon_use_rtype = False

# The look: the pydata theme, as the KaxaNuk Data Curator's documentation has.
html_theme = 'pydata_sphinx_theme'
