Object Matrix Input
===================

Description
-----------

This node returns the transformation matrix of the input object. Matrices are more reliable than transforms because of their different forms and because they are always up to date even during physics simulations.

.. image:: images/matrix_input_node.png
   :width: 160pt

Inputs
------

- **Object** - An object.

Outputs
-------

- **World** - World space transformation matrix.
- **Basis** - World space transformation matrix but without constraints and parenting.
- **Local** - Local space transformation matrix.
- **Parent Inverse** - Inverse of object’s parent matrix at time of parenting.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/object_matrix_input_node_example.gif
