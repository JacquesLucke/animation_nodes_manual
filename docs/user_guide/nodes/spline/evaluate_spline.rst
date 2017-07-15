Evaluate Spline
===============

Description
-----------

This node will return the position and the tangent line of a point on the curve at some normalized distance from the starting point where this distance is defined by the input **Parameter**.

.. image:: images/evaluate_spline_node.png
   :width: 160pt

.. include:: /includes/nodes/uniform_vs_resolution.rst

Inputs
------

- **Spline** - A spline to evaluate.
- **Parameter** - The position of the point to be evaluated in the normalized distance of the spline. (0 is the start of the spline and 1 is the end of the spline)

Outputs
-------

- **Location** - A vector that represents the position of the point in the curve that correspond to the input parameter.
- **Tangent** - A vector that is aligned with the tangent line to the evaluated point.

Advanced Node Settings
----------------------

- **Resolution** - It is the quality of the evaluated spline, in other words, it is the number of point in the spline used in evaluation.

Examples of Usage
-----------------

.. image:: gifs/evaluate_spline_node_example.gif
