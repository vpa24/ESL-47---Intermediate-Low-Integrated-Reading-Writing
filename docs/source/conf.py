# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ESL47'

# -- General configuration

extensions = [
	'recommonmark',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# Add your custom CSS files to the html_css_files list.
html_css_files = [
    'css/custom.css',
]
# -- Options for EPUB output
epub_show_urls = 'footnote'

# Specify the source_suffix for Markdown files.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Specify the master doc (the main entry point for your documentation).
# master_doc = 'index'