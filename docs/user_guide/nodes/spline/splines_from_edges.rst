Spline From edges
=================

Description
-----------

This node creates a linear poly spline for every input edge, that is, every edge will represent a linear poly spline that have 2 point which are the vertices of the edge.

.. image:: images/splines_from_edges_node.png
   :width: 160pt

Inputs
------

- **Vertices** - A vector list that represent the position of the vertices of the edges.
- **Edge Indices** - An Edge Indices list.
- **Radius** - A float list that contains the radii of each poly spline (edge).

Outputs
-------

- **Splines** - The output splines.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/splines_from_edges_node_example.gif
