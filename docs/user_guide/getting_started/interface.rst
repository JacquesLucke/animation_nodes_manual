*********
Interface
*********

Much of the interface is located in the node editor in blender while some of the interface exist in other regiones like the 3D viewport.


Node Menu
=========

To add a new node, you can open the Node Menu by pressing ``Shift+A`` like other node systems. The menu contain lots of submenus for better categorizing, the first cluster of submenus includes data processing node, the second cluster includes node that can communicate with blender (Write and read blender data). The menu include all node in AN except for passive nodes which are usually added automatically or by searching for them, such nodes are like the **Converter** and **Convert To Integer List** nodes.

  .. image:: images/node_menu.png


Node Search
===========

The search box can be opened by pressing ``ctrl-A``, it enables you to quickly find and insert nodes by
their name. Some nodes have multiple search tags to make it easier to find them. Search box can find any node in AN even if they were passive from the node menu.

  .. image:: images/search_menu.png


Node Settings
=============

Nodes include multiple settings types, settings that usually changes per node are drawn inside nodes directly for faster workflow, settings that doesn't change much per node are drawn in a custom panel in the properties menu to avoid clustering the UI.

Inside the Node
^^^^^^^^^^^^^^^

Settings that usually changes ar drawn inside nodes, for example:

  .. image:: images/inside_node_settings.png

Advanced Node Settings
^^^^^^^^^^^^^^^^^^^^^^

Settings that doesn't change much per node are drawn in a custom panel called
**Advanced Node Settings**. The settings inside are always for the currently
active node.

  .. image:: images/advanced_node_settings.png

It is usually the case that you need to make elements copies, so this option is moved to the advanced node settings to avoid clustering. Furthermore, the node changes type automatically, so the change type operator are not always needed.

Node Panel
^^^^^^^^^^

Sockets (Inputs and Output) of every node can be hidden or unhidden through this panel by pressing the "eye" next to the desired socket. Some nodes subprograms inputs allow reordering of sockets by using the **arrows**.
You can also specify the name and lable of the node from this panel. Name has to be unique.

  .. image:: images/node_panel.png

Tree Settings
=============

The tool menu in the node editor in Animation Nodes contain settings and information regarding the nodetree itself and nit individual nodes.

  .. image:: images/nodetree_menu.png

Auto Execution Panel
^^^^^^^^^^^^^^^^^^^^

Includes options related to auto execution of the node tree.

Developer
^^^^^^^^^

Includes options related to inspecting and profilling and debugging node trees.

Overview
^^^^^^^^

Includes some information about the node tree like the execution time. The statistics button draws a table that include information about the number of nodes in the node tree. Try it out to see overview of your node tree.

Animation Nodes Tree
^^^^^^^^^^^^^^^^^^^^

This panel include manual execution button and the scene that the nodee tree belongs too.

- **Edite Node labels** - If enabled, a text box will appear in every node that lets you edit the label of the node. This is helpful if you want to organize you node tree after you finish building it.

3D View
=======

  .. image:: images/3dview_menu.png

ID
^^

Includes some options related to some specific nodes like the ID node.

Data Input
^^^^^^^^^^

Display the the data input nodes (like integer input) inside the panel if Show In Viewport is enabled. (See one of the data input nodes)
