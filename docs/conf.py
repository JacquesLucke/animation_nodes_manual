import sys
import os

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['ytemplates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Animation Nodes Documentation'
copyright = u'2014, Jacques Lucke'

version = '0.0.1'
release = '0.0.1'

exclude_patterns = []

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['ystatic']

htmlhelp_basename = 'AnimationNodesDocumentationdoc'


latex_elements = {
latex_documents = [
  ('index', 'AnimationNodesDocumentation.tex', u'Animation Nodes Documentation Documentation',
   u'Jacques Lucke', 'manual'),
]

man_pages = [
    ('index', 'animationnodesdocumentation', u'Animation Nodes Documentation Documentation',
     [u'Jacques Lucke'], 1)
]
texinfo_documents = [
  ('index', 'AnimationNodesDocumentation', u'Animation Nodes Documentation Documentation',
   u'Jacques Lucke', 'AnimationNodesDocumentation', 'One line description of project.',
   'Miscellaneous'),
]

epub_title = u'Animation Nodes Documentation'
epub_author = u'Jacques Lucke'
epub_publisher = u'Jacques Lucke'
epub_copyright = u'2014, Jacques Lucke'
epub_exclude_files = ['search.html']

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True
