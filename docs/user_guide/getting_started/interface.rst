*********
Interface
*********

On this page I want to give a quick overview where you to find everything
that has to do with this addon in Blender. Obviously most settings are
located in the node editor but not all of them.


Node Menu
=========

The menu to insert new nodes opens when pressing ``shift-A`` like in the
compositing and material nodes. The menu is fairly large with many submenus.
It is not ideal for a quick workflow but it helps when you forgot the name
of a node.

  .. image:: node_menu.PNG


Node Search
===========

The search box (``ctrl-A``) enables you to quickly find and insert nodes by
their name. Some nodes have multiple search tags to make it easier to find them.
Also here are all installed nodes. Not only a subset like in the menu.

  .. image:: node_search.PNG


Node Settings
=============

Inside the node
^^^^^^^^^^^^^^^

Directly in the node are all the sockets that can be linked with other nodes.
Also sometimes there are additional properties you should care about.

  .. image:: settings_inside_node.PNG

Advanced node settings
^^^^^^^^^^^^^^^^^^^^^^

Some nodes have settings which aren't very useful most of the time but can
become very handy under certain circumstances. Putting all these properties
directly in the node would clutter the UI a lot. A better solution is to have
these properties in an extra panel in the right properties bar. The panel is called
``Advanced Node Settings``. The settings inside are always for the currently
active node. I suggest to put this panel at the top.

  .. image:: advanced_node_settings_panel.PNG
