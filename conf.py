# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import shutil
# sys.path.insert(0, os.path.abspath('../../src/'))

# Copy notebooks
# shutil.copytree('../../notebooks', 'notebooks', dirs_exist_ok=True)

project = 'Course 41934'
copyright = '2024, DTU'
author = 'DTU Construct'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    'nbsphinx',
    ]

autosectionlabel_prefix_document = True
autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

autodoc_default_flags = ['members', 'undoc-members' ]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'press'
GITHUB_URL ="https://github.com/timmcginley/41934"
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": GITHUB_URL,
    "use_repository_button": True,
    # "use_edit_page_button": True,
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": GITHUB_URL,  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
   ]
}

html_static_path = ['_static']
