"""Sphinx configuration."""
project = "Splinterglyph"
author = "Bill Bradley"
copyright = "2023, Bill Bradley"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
