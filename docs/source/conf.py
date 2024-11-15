# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Analog Course'
copyright = '2024, Adrien Luitot'
author = 'Adrien Luitot'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_toolbox.sidebar_links',
    'sphinx_design',
    'sphinx_toolbox.code',
    'sphinx_toolbox.github'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Used to show GitHub repo on the side bar
github_username = 'adrienluitot'
github_repository = 'analog-course'