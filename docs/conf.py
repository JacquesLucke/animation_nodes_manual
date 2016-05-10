import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo'
]

todo_include_todos = True

templates_path = ['ytemplates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Animation Nodes'
copyright = u'2015, Jacques Lucke'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = ['includes/*']

pygments_style = 'sphinx'

htmlhelp_basename = 'AnimationNodesdoc'

latex_elements = {}
latex_documents = [
  ('index', 'AnimationNodes.tex', u'Animation Nodes Documentation',
   u'Jacques Lucke', 'manual'),
]

man_pages = [
    ('index', 'animationnodes', u'Animation Nodes Documentation',
     [u'Jacques Lucke'], 1)
]
texinfo_documents = [
  ('index', 'AnimationNodes', u'Animation Nodes Documentation',
   u'Jacques Lucke', 'AnimationNodes', 'A new way to work with data in Blender.',
   'Miscellaneous'),
]

epub_title = u'Animation Nodes'
epub_author = u'Jacques Lucke'
epub_publisher = u'Jacques Lucke'
epub_copyright = u'2014, Jacques Lucke'
epub_exclude_files = ['search.html']
