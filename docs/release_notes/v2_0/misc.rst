Misc
****

Sockets
=======

New socket type: **Falloff**.

Removed socket types: **Vertex**, **Polygon**.

The **BMesh** socket has a new color.

Data Inputs
===========

Input of data input nodes like input integer, float are now hidden because it confuses people. It can be unhidden just like any node if needed.

.. image:: images/input_nodes.png

Converter
=========

Converter node now has a lock button to lock the data type and stop it from changing the output socket automatically.

.. image:: images/converter.png

Loops Generator Output
======================

Generators are now vectorized which means they can append multiple values if given a list.

.. image:: images/loops.png

Groups
======

In the Group Input node the socket is renamed from *New Parameter* to *New Input*.

In Group Output node, the socket is renamed from *New Return* to *New Output*.

Expression
==========

There are two new advanced settings:

- Inline Expression
    Reduces function call overhead. The speedup is only notable when the expression is very small. When deactivated expressions like ``sin(x)`` can be used. To archieve the same thing when the setting is activated use ``math.sin(x)``.
- Fixed Data Type
    Forbid the node to change the output type automatically. This is automatically activated when the output type is selected manually.

.. image:: images/expression_node.png

Keyboard Shortcuts
==================

Animation Nodes currently uses the *W*, *E* and *U* key in the node editor. The *W* and *E* key have not changed since the last release but the *U* key now opens a popup that not only shows the advanced settings of a node but also its sockets. This is useful as some nodes have hidden sockets or allow reordering/deletion of sockets.

.. image:: images/socket_settings.gif

3D Viewport
===========

An option to show the indices of vertices, edges and polygons indices is available under the display panel in properties menu now. Note that this option is designed to be used in object mode.

.. image:: images/viewport_indices.png

Templates
=========

Templates were removed. There will be a better template system in the future.

Remove Node Tree
================

There is now a button to remove the current node tree.

.. image:: images/remove_button.png

Measure Execution Time
======================

The Measure Execution Time tool now displays the minimum execution time instead of average.

.. image:: images/measure_execution_times.png

Performance Mode
================

Performance Mode was removed. It was absolutely useless for users.
