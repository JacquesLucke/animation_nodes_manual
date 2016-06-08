Script
======

.. include:: /includes/workinprogress.rst
.. todo:: unfinished content in file user_guide/nodes/subprograms/script.rst


.. image:: script_input_nodes.png

Begin by adding a script node, and connecting the script node to a text datablock, created with the Blender text editor. To add input or output variables, use the New Input and New Ouput buttons on the node UI. The input and output names are automatically mapped to global variables in your script. Once input and output variables are configured, you can invoke your script by finding its name under Subprograms-InvokeSubprogram. Here is an example of a very simple script.

.. image:: script_ex1.jpg


Importing Animation Nodes Datatypes
-----------------------------------

Because Animation Nodes is normally installed at "animation_nodes-master", you can't import it using the normal import statement. Dash (-) is not an allowed character in normal module names. To import parts of AN at it's default install location, you can do the following. This is the preferred way to do an import, because this will work inside and outside of script contexts, so it will work if you press "Run Script" in a text editor.::

    import importlib
    PolySpline = importlib.import_module("animation_nodes-master.data_structures.splines.poly_spline")

If you have a simple script which doesn't need any debugging, you can simplify this a bit, because the animation_nodes module is already imported into the namespace of AN script nodes. Within the script context only, you can access portions of AN using statements like the one below. However, this will not work outside of the AN script node execution context, such as when you click "Run Script".::

    PolySpline = animation_nodes.data_structures.splines.poly_spline

