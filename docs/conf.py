import sys
import os

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['ytemplates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Animation Nodes'
copyright = u'2014, Jacques Lucke'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = []

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['ystatic']

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