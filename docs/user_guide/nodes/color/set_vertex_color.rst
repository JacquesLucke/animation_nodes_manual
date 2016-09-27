Set Vertex Color
================

Description
-----------
This node create a vertex color layer and fill it with a single color.

.. image:: images/set_vertex_color_node.png
   :width: 160pt

Inputs
------

- **Object** - The object that will carry the vertex color layer.
- **Color** - The color of each vertex of the object.


Outputs
-------

- **Object** - The input object.

Advanced Node Settings
----------------------

- **Check Color**
    If this is enabled, Animation Nodes will check if the color haven't changed
    before setting the new color. If it haven't, Animation Nodes will return the
    object without any change.

    This will result a speed up in the execution time if you are not changing
    the color. So make sure to check it if you want to speed up the calculation time.

Note
----

If the name you entered in the vetex color layer is the name of an existing
vertex color layer, Animation nodes will overwrite the data of this layer
instead of creating a new one.

Examples of Usage
-----------------

See other nodes in the color category.
