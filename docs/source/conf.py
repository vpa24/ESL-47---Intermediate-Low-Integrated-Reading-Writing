# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ESL47'

release = '0.1'
version = '0.1.0'

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

html_theme_options = {
    'navigation_depth': 4,  # Customize the depth of the navigation menu.
    'display_version': True,
    'logo_only': False,
}

# Add more links to the navigation menu.
html_sidebars = {
    '**': [
        'index.html',  # Related Pages
        'api.html',  # Table of Contents
        'usage.html',  # Source Link
        'search.html',  # Search Box
        'unit1.html',  # Your custom sidebar file (optional)
    ],
}
# -- Options for EPUB output
epub_show_urls = 'footnote'

# Specify the source_suffix for Markdown files.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Specify the master doc (the main entry point for your documentation).
master_doc = 'index'