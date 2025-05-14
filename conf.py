# -*- coding: utf-8 -*-
#
# Mole Engine documentation build configuration file

import sys
import os

# -- General configuration ------------------------------------------------

needs_sphinx = "1.3"

# Sphinx extension module names and templates location
sys.path.append(os.path.abspath("_extensions"))
extensions = [
    "moscript",
    "mole_descriptions",
]
templates_path = ["_templates"]

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = ".rst"
source_encoding = "utf-8-sig"

# The master toctree document
master_doc = "index"

# General information about the project
project = "Mole Engine"
copyright = (
    "2024, NKDuy and the Mole community (CC-BY 3.0)"
)
author = "NKDuy and the Mole community"

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = os.getenv("READTHEDOCS_VERSION", "2.1")
# The full version, including alpha/beta/rc tags
release = version

# Language / i18n

supported_languages = {
    "en": "Mole Engine (%s) documentation in English",
}

language = os.getenv("READTHEDOCS_LANGUAGE", "en")
if not language in supported_languages.keys():
    print("Unknown language: " + language)
    print("Supported languages: " + ", ".join(supported_languages.keys()))
    print(
        "The configured language is either wrong, or it should be added to supported_languages in conf.py. Falling back to 'en'."
    )
    language = "en"

exclude_patterns = ["_build"]

# fmt: off
# These imports should *not* be moved to the start of the file,
# they depend on the sys.path.append call registering "extensions".
from moscript import MoScriptLexer
from sphinx.highlighting import lexers

lexers['moscript'] = MoScriptLexer()
# fmt: on

# Pygments (syntax highlighting) style to use
pygments_style = "sphinx"
highlight_language = "moscript"

# -- Options for HTML output ----------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
if on_rtd:
    using_rtd_theme = True

# Theme options
html_theme_options = {
    # 'typekit_id': 'hiw1hhg',
    # 'analytics_id': '',
    # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
    "logo_only": True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    "collapse_navigation": False,  # Collapse navigation (False makes it tree-like)
    # 'display_version': True,  # Display the docs version
    # 'navigation_depth': 4,  # Depth of the headers shown in the navigation bar
}

html_title = supported_languages[language] % version

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
    "display_github": False,  # Integrate GitHub
    "github_user": "",  # Username
    "github_repo": "",  # Repo name
    "github_version": "",  # Version
    "conf_py_path": "/",  # Path in the checkout to the docs root
    "mole_inject_language_links": True,
    "mole_docs_supported_languages": list(supported_languages.keys()),
    "mole_docs_basepath": "https://moleengine-docs.web.app/",
    "mole_docs_suffix": ".html",
    "mole_default_lang": "en",
    "mole_canonical_version": "stable",
    # Distinguish local development website from production website.
    # This prevents people from looking for changes on the production website after making local changes :)
    "mole_title_prefix": "" if on_rtd else "(DEV) ",
}

html_logo = "img/docs_logo.png"

# Output file base name for HTML help builder
htmlhelp_basename = "MoleEnginedoc"

# -- Options for reStructuredText parser ----------------------------------

# Enable directives that insert the contents of external files
file_insertion_enabled = False

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "MoleEngine.tex",
        "Mole Engine Documentation",
        "NKDuy and the Mole community",
        "manual",
    ),
]
