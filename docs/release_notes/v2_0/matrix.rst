Matrices
********

Distribute Matrices
===================

This node was newly added and it generate a list of transformation matrices distributed on a line, grid, circle or mesh vertices. The resulted transformation matrices include locations information only in the line and grid options while it include both location and rotation data in the circle and mesh vertices options assuming vertices normal were given.

.. image:: images/distribute_matrices.gif

Replicate Matrix
================

This node was newly added and it instance and transforms input transfromation matrices based on some other input transfromation matrices. Below is an example if use, the first distribute matrices generate a circle of matrices, the replicate matrix node was used to instance those circles in some other bigger circle generated from the second distribute matrix.

.. image:: images/replicate_matrix.gif

Transform Matrix
================

This node transforms a matrix (or matrix list) by another matrix input.

.. image:: images/transform_matrix.gif

Offset Matrices
===============

This newly added node make use of falloffs with matrices. The node simply transforms the input transformation matrices based on a transformation matrix generated from the input translation, rotation and scale vectors and eulers, the factor of transformation is controlled by a falloff.

.. image:: images/falloff_example.gif

Change Matrix Pivot
===================

Change Matrix Pivot node was removed because it can be recreated easily with ordered matrix multiplication.
