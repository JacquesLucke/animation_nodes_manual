Script
======

.. include:: /includes/workinprogress.rst
.. todo:: No content in file user_guide/nodes/subprograms/script.rst

Because Animation Nodes is normally installed at "animation_nodes-master", you can't import it using the normal import statement. Dash (-) is not an allowed character in normal module names. To import parts of AN at it's default install location, you can do the following. This is the preferred way to do an import, because this will work inside and outside of script contexts, so it will work if you press "Run Script" in a text editor.::

    import importlib
    PolySpline = importlib.import_module("animation_nodes-master.data_structures.splines.poly_spline")

If you have a simple script which doesn't need any debugging, you can simplify this a bit, because the animation_nodes module is already imported into the namespace of AN script nodes. Within the script context only, you can access portions of AN using statements like the one below. However, this will not work outside of the AN script node execution context, such as when you click "Run Script".::

    PolySpline = animation_nodes.data_structures.splines.poly_spline

