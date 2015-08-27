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

Inside the Node
^^^^^^^^^^^^^^^

Directly in the node are all the sockets that can be linked with other nodes.
Also sometimes there are additional properties you should care about.

  .. image:: settings_inside_node.PNG

Advanced Node Settings
^^^^^^^^^^^^^^^^^^^^^^

Some nodes have settings which aren't very useful most of the time but can
become very handy under certain circumstances. Putting all these properties
directly in the node would clutter the UI a lot. A better solution is to have
these properties in an extra panel in the right properties bar. The panel is called
``Advanced Node Settings``. The settings inside are always for the currently
active node. I suggest to put this panel at the top.

  .. image:: advanced_node_settings_panel.PNG

Generic Node Panel
^^^^^^^^^^^^^^^^^^

There are a few properties that all animation nodes have in common. I extended
the ``Node`` panel to give you access to these. I recommend to drag this panel
directly under the Advanced Node Settings panel.

  .. image:: generic_node_panel.PNG

Some nodes allow you to remove and reorder individual sockets. Also hiding sockets
you don't need can improve the look of your node tree. Some nodes hide sockets
by default because you need them only in rare cases.

If the active node allows some customization of the sockets you can also expose
the operators to do so into the node. (To test this you can create an expression
node, make some sockets and press the buttons below `Toogle Operation Visibility`)

The identifier at the button may not be important for you. It is more for developers.


Tree Settings
=============

Animation Node Tree Panel
^^^^^^^^^^^^^^^^^^^^^^^^^

This panel does not have many functions yet. If you don't use `Auto Execution`
you can execute the currently active node tree. Executing a tree means to
execute all `Main` networks. That includes everything except `Groups`, `Loops`.
The time below shows the time it took to execute.

Auto Execution Panel
^^^^^^^^^^^^^^^^^^^^

Most of the time you do animations you want `Auto Execution` to be enabled.
That automatically executes the same nodes the `Execute Node Tree` would execute.
The execution is triggered by different events. See the tooltips for more information.

  .. image:: tree_settings_panel.PNG
