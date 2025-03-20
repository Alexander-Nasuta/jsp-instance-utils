# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'jsp-instance-utils'
copyright = '2025, Alexander Nasuta'
author = 'Alexander Nasuta'
release = '1.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",

    "sphinx.ext.duration",
    "sphinx_copybutton",

    "sphinx.ext.autosectionlabel",

    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",

    "sphinx.ext.autodoc",

    "sphinx.ext.napoleon",

    "nbsphinx",
]


templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = f"JSP Benchmark Instances"
html_static_path = ['_static']
html_theme_options = {
    "light_logo": "logo-light.png",
    "dark_logo": "logo-light.png",
}
html_css_files = [
    'custom.css',
]

# Configure autosectionlabel
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Exclude specific files
autosectionlabel_exclude_files = ['README.md']
