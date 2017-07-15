Find Nearest Points
===================

Description
-----------

This node finds the nearest points in the input KD Tree to a given point.

.. image:: images/find_nearest_points_node.png
   :width: 160pt

Inputs
------

- **KD Tree** - A KD tree that contain your points.
- **Amount** - The amount of points to search for.
- **Vector** - A vector that represent the location of the point in which we want to find its nearest points.

Outputs
-------

- **Vectors** - The locations of the points that is nearest to the input point.
- **Distances** - The distances between the output points and the input point.
- **Index** - The indices of the nearest points to the input point in the list used to construct the KD tree.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/find_nearest_points_node_example.gif
