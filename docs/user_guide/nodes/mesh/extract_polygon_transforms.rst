Extract Polygon Transforms
==========================

Description
-----------

This node returns transformation matrices that describe the location and orientation of the input polygons. The local x axis is aligned with the direction of the first edge of each polygon.

.. image:: images/extract_polygon_transforms_node.png
   :width: 160pt

Inputs
------

- **Vertices Locations** - A vector list that represent the the locations of the vertices of the polygons.
- **Polygon Indices** - The polygon indices of the polygons.

Outputs
-------

- **Transforms** - A matrix list that include transformation matrices that describe the location and orientation of the polygons.
- **Inverse Transforms** - The inverse matrix of the transforms.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/extract_polygon_transforms_node_example.gif
