# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'StratiGraph Server'
copyright = '2026, Emanuel Demetrescu (CNR-ISPC) and the StratiGraph consortium'
author = 'Emanuel Demetrescu'

release = '1.6'
version = '1.6.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    # reusable RST snippets, pulled in with `.. include::`, never pages
    '_includes/**',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

numfig = True

# -- AI Act Article 50 transparency footer -----------------------------
# A short notice appended to every page via ``rst_epilog``, pointing to
# the project's AI usage policy at extendedmatrix.org/ai-usage/.
rst_epilog = """
.. include:: /_includes/ai_usage_notice.rst
"""
