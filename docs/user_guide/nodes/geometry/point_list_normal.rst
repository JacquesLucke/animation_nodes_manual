Point List Normal
=================

Description
-----------
This node takes multiple vectors which represent points of a polygon and return the normal of that polygon.

At least 3 points are needed to compute the normal. If more than 3 points were input, the resulted normal will be the average of the normals of each 3 points.

.. image:: images/point_list_normal_node.png
   :width: 160pt

Inputs
------

- **Point List** - A vector list that contain the locations of the polygon points.

Outputs
-------

- **Normal** - A unit vector that represent the normal of the polygon. A zero vector if points weren't valid.
- **Is Valid** - A boolean which is True if blender was able to calculate the normal.

Advanced Node Settings
----------------------

- N/A

Notes
-----

The order of points matter as cross product is used to compute the normals, So points in reversed order will return a normal that is in the reverse direction of the normal computed by the original list.

Examples of Usage
-----------------

.. image:: gifs/point_list_normal_node_example.gif
