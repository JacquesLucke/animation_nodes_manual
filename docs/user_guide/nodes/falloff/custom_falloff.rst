Custom Falloff
==============

Description
-----------

This node creates an index based falloff that associates the first element from the float list to the first object, second element to the second object and so on.

.. image:: images/custom_falloff_node.png
   :width: 160pt

Inputs
------

- **Strengths** - A float list the represents the floats of the objects. If the number of object is greater than the length of this list, extra object will have a floats equal to the input fallback value.
- **Fallback** - The fallback value.

Outputs
-------

- **Falloff** - The actual falloff object.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/custom_falloff_node_example.gif
