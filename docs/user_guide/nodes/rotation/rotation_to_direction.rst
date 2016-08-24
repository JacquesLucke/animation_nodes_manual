Rotation To Direction
=====================

Description
-----------
This node convert input rotation to a corresponding vector.

.. image:: images/rotation_to_direction_node.png
   :width: 160pt

Demonstration
-------------
To better understand how this node work, you can think of it as follow, It basically get you the local selected axis of the object.

In this example you can see that the resulte vector is always aligned to the selected axis which is Z in this case.

.. image:: gifs/rotation_to_direction_node_demonstration.gif

Inputs
------
 
- **Rotation** - The rotation that define the direction.
- **Length** - The magnitude of the resulted vector.

Outputs
-------

- **Direction** - The resulted vector.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/rotation_to_direction_node_example.gif
