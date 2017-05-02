Change Matrix Pivot
===================

Description
-----------

This node includes 5 operations which perform multiple consecutive transformations that changes the pivot of the input transformation matrix.

.. image:: images/change_matrix_pivot_node.png
   :width: 160pt

Demonstration
-------------

Technically, there is no such thing as a **Pivot** in mathematics. There is a constant never changing pivot which is the **Origin** of the coordinates space (point ``(0,0,0)``). However we can perform a series of fake transformations to change the pivot of the original transformation.

**Example**: Suppose we have a cube at position ``(2,2,0)``, if you multiplied the matrix of the cube by a **Z axis rotation transformation matrix**, the cube will rotate around the origin point which is ``(0,0,0)`` and its location will change relative to that origin.

Suppose we want the pivot of the transformation to be ``(2,2,0)`` which is the same location as the cube. We said before that the pivot for any transformation is constant and can never be changed. Mathematicians thought about that and said "If we can't move the pivot to the object why not move the object to the pivot, do the transformation and move it back".

So the solution become clear, if we have an object at ``(2,2,0)`` and we want the origin to be at ``(2,2,0)``, we move the object to the origin, do the transformation and move it back to where it was.

.. image:: gifs/change_matrix_pivot_node_example_2.gif

Options
-------

- **Pivot Matrix** - This option lets you change the pivot using a transformation matrix. This will allow you to set a parent child relation between the matrix and the pivot matrix. The location of the pivot matrix does not affect the pivot, however, the rotation and the scale are affected relative to the point ``(0,0,0)``.

.. image:: gifs/change_matrix_pivot_node_example_3.gif

- **Pivot Location** - This option lets you set the location of the pivot in 3D space.

.. image:: gifs/change_matrix_pivot_node_example_4.gif

- **Center And Rotation** - This option lets you set the pivot of the transformation matrix and rotate around it based on the input euler. Note that the center is relative to the original location of the object, so if you want to set an absolute center, subtract the location from the center.

.. image:: gifs/change_matrix_pivot_node_example_5.gif

- **X Line,Z Direction** - This option lets you orient the local space of the transformation matrix to a specific orientation based on 2 vectors, a vector which represent the center of the space and thus the pivot and another that define the x axis of the local space as well as a normal vector which define to the local z axis of the local space. The default value for the normal vector is ``(0,0,1)`` which aligns the the local Z axis with the global Z axis which is the standard orientation, however if you change the the normal to be ``(1,0,0)`` this means you are aligning the local Z axis with the global X axis which means a rotation around the Z axis actually correspond to a rotation around the X axis.

.. image:: gifs/change_matrix_pivot_node_example_6.gif

- **X Line, Z line** - This is exactly like **X Line,Z Direction** explained above, but instead of the normal vector you have a line that defines the Z orientation.

Inputs
------

- **Transformation matrix** - A transformation matrix to change its pivot.

(Inputs are based on the type of the node)


Outputs
-------

- **Transformation matrix** - The transformation matrix after pivot change.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/change_matrix_pivot_node_example.gif
