*********
Execution
*********

Animation Nodes takes you nodes tree and convert it into code then execute that code to see the actual result of it.

You may notice that when you start using AN, a number is changing very rapidly at the top left corder of the node editor, that number is the time it took to execute the node tree.

By default, AN execute the node tree as much as possible for the best and smoothest update of the scene. However, this exhauste the CPU and slows down other areas in blender. It doesn't make sense to execute the node tree even if nothing changes in your node tree or the scene, so executing the node tree that much may not be needed.

Animation Nodes provide you with an automatic and a manual execution systems that suite you workflow. Possible execution systems are listed below.

Automatic Execution
===================

By default auto execution is enabled and cab be found in the auto execution panel in the tool menu.

Always
------

Always option is enabled by default and it does what we stated before, that is, execute the node tree as much as possible. This option should never be used unless absolutely needed. A possible uses for it is as follows:

- A lot of variables in the scene are changing regularly and constantly assuming AN uses them. If they are just couple of variables then triggers should be used, see below.
- When running a simulation that need to run constantly, for instance, when simulating a system using eulers method.

.. image:: gifs/always.gif

Notice how AN execute (execution time changes) constantly even if nothing is changing.

If always is disabled, then you have multiple options described below.

Tree Changed
------------

If enabled, the node tree will execute everytime the node tree changes, that is, a node is added or removed. You probably want to enable this after you disable alwayse because it is probable that you need to execute the node tree everytime you change something in your tree.

.. image:: gifs/tree_changed.gif

Notice how the tree execute when I add a new node.

Frame Changed
-------------

If enabled, the node tree will execute everytime the current frame of the scene changes. You probably want to enable this when ever you have a node tree that depend on time.

.. image:: gifs/frame_changed.gif

Notice how the tree execute when ever the current frame changes.

Property Changed
----------------

If enabled, the node tree will execute everytime a property changes, that is, an input or an option of the node is changed. You probably want to enable this after you disable alwayse because it is probable that you need to execute the node tree everytime you change something in your tree. Notice that chaning a value in the advanced node settings won't necessarily execute the node tree even if this option is enabled.

.. image:: gifs/property_changed.gif

Notice how the tree execute when I change a value in the node tree.

Minimum Time Difference
-----------------------

This value defines the time between each two consecutive executions.

Triggers
--------

Triggers are basically “watchers” that are hired by you to watch for a change in some property you told them to watch. They tell AN to execute the node tree everytime the property they watch change.

For instance, lets say I am using the location of a cube object in my node tree and I want to execute everytime the location changes, so I simply add a trigger and tell it to watch for the location of the cube object.

.. image:: gifs/triggers.gif

There are two options:

- **Object Property** - An object is choosen and the property ID is defined relative to it. An example for such IDs are: ``location``, ``euler_rotation``, ``location.x`` ... .
- **Scene Property** - The peth of the property has to be fully defined, for instance, ``bpy.data.objects["Cube"].modifiers["Subsurf"].levels`` whic watches for the subsurface levels of a modifier.

Errors
======

During the execution of the node tree, some errors may be encountered, those errors can either be fatal or not, below is a presentation for both.

NonFatal Error
--------------

Those errors are reported inside nodes and they does not stop execution, an example:

.. image:: images/nonfatal-errors.png

The barycentric node simply expect 3 vectors for the source inputs but not were given, to fix the error, just input a vector list. When such eeror occure, the node either does nothing or return the default value of the output, since the output is a vector in thise case, then it is initialized by the vector ``(0,0,0)``.

Fatal Errors
------------

Fatal errors stop the execution of the whole node tree and have to be solved. Such errors occure when you try to do something with a node that the developers didn't put in consideration, it could laso be a bug and should be reported in that case. An example for such error can be seen in the expression node:

.. image:: images/fatal_error.png

The expression node has an option to Debug the expressions you write before executing them. I disabled it for the second one and intentionally made a sytax error. The first node reported the error and didn't stop the execution (A non-fata error), the second node however stoped the execution and colored the node editor's borders red to indicate a fatal error. To fix that error you just solve the syntax error or just enable debug option.
