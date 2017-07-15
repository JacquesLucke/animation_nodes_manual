Matrix List
===========

Description
-----------

This node is used to create an arbitrary list of matrices. A new matrix can be added with the *New Input* button. A new matrix can also be added by plugging it into the transparent socket.

.. image:: images/matrix_list_node.png
   :width: 160pt

Inputs
------

- **Matrix** - A matrix at the index 0.
- **Matrix** - A matrix at the index 1.
- **Matrix** - ...

Outputs
-------

- **matrix list** - A list that contains all the input matrices.

Advanced Node Settings
----------------------

- **Change type** - Changes the type of the float list to another list type.
- **Hide Inputs** - Hides all the inputs in the node.
- **Remove Unlinked Inputs** - Removes all the inputs that are not connected to another node.

Caution
-------

A warning will pop up when you use the *Remove Unlinked Inputs* button in the node, while if you used the the *Remove Unlinked Inputs* button in the *Advanced Node Settings* the inputs will be removed without a warning.

Examples of Usage
-----------------

.. image:: gifs/combine_matrices_node_example.gif
