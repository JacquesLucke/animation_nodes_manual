Fade Falloff
============

Creates a falloff that makes a smooth transition between two influences based on the position in a list.

.. image:: images/fade_falloff_node.png

The three different modes the node provides are just for convenience to have less math nodes in the network.

Inputs
------

The first two inputs specify the the range in which the fade takes place. Which sockets there are specifically depends on the selected mode.

The **Start Value** and **End Value** inputs specify from where to where the node interpolates the values.

The **Interpolation** input allows to modify how the fade will look like.

Outputs
-------

- **Falloff** - The actual falloff object.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

Fade out another falloff by combining this node with a **Mix Falloffs** node:

    .. image:: images/fade_rotation_example.png
