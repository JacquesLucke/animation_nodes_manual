*********
Interface
*********

Much of the interface is located in the node editor while the rest of the interface exist in other regions like the 3D viewport.

.. image:: images/node_editor.png

Animation Nodes have its own node editor type which you can select by clicking on the Dope Sheet icon in the tool bar. A new node tree can be added by clicking on the **New** button.

Node Menu
=========

To add a new node, you can open the Node Menu by pressing ``Shift+A`` just like other node systems. The menu contains a group of submenus each of which contains a list of node categorize by their type. The menu includes all nodes in Animation Nodes except for some *passive nodes*, passive node are node that can only be added through the **Node Search** which is covered in the next section.

.. image:: images/node_menu.png

Passive nodes are usually added automatically when ever needed, for instance, *Parse Number* node is automatically added when attempting to connect a text type to a number type:

.. image:: gifs/passive_node.gif

Node Search
===========

The search box can be opened by pressing ``Ctrl-A``, it enables you to quickly find and insert nodes by their names. Some nodes have multiple search tags to make it easier to find, for instance, searching for "Add, subtract, multiply, ..." will show math nodes. Search box can find any node in Animation Nodes even if it was passive.

.. image:: images/search_menu.png

Node Settings
=============

Nodes include multiple settings types, options that users use often are drawn inside nodes directly for faster workflow, options that users don't use often are drawn in a custom panel in the properties (N) menu to avoid clustering the UI.

Inside the Node
^^^^^^^^^^^^^^^

Options that users use often are drawn inside nodes, for example:

.. image:: images/inside_node_settings.png

Math operation and distribution patterns are node options.

Advanced Node Settings
^^^^^^^^^^^^^^^^^^^^^^

Options that users don't use often are drawn in a custom panel called **Advanced Node Settings**.

.. image:: images/advanced_node_settings.png

Node Panel
^^^^^^^^^^

Sockets (Inputs and Outputs) of nodes can be hidden or unhidden through this panel by pressing the "eye" next to the desired socket. Some nodes like subprograms, allows reordering of sockets by using the **arrows**. You can also change the name and label of nodes in this panel, names has to be unique.

  .. image:: images/node_panel.png

Tree Settings
=============

The tool menu in the node editor in Animation Nodes contain settings and information regarding the nodetree itself and not individual nodes. All of the options will be explained in other sections of the getting started guide.

.. image:: images/nodetree_menu.png

Auto Execution Panel
^^^^^^^^^^^^^^^^^^^^

Include options related to auto execution of the node tree.

Developer
^^^^^^^^^

Include options related to inspecting, profilling and debugging node trees.

Overview
^^^^^^^^

Include some information about the node tree like the execution time. The statistics button draws a table that include information about the number and types of nodes in the node tree.

Animation Nodes Tree
^^^^^^^^^^^^^^^^^^^^

This panel includes manual execution button and the scene that the node tree belongs too.

- **Edite Node labels** - If enabled, a text box will appear in every node that lets you edit the label of the node. This is particularly helpful if you want to organize you node tree after you finished building it.

3D View
=======

.. image:: images/3dview_menu.png

ID
^^

Includes some options related to the **ID Key** node.

Data Input
^^^^^^^^^^

Displays the the data input nodes inside the panel if **Show In Viewport** is enabled. (See one of the data input nodes)
