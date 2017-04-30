Map Range
=========

Description
-----------

This node remaps a value from a defined interval to a new interval.
Every value has a relative position in a specific interval, this node find a new value that match the relative position but in a new defined interval.

.. image:: images/map_range_node.png
   :width: 160pt

Inputs
------

- **Value** - A float that should be remaped.
- **Input Min** - The start of the original interval.
- **Input Max** - The end of the original interval.
- **Output Min** - The start of the new interval.
- **Output Max** - The end of the new interval.
- **Interpolation** - If interpolation is enabled, the output value will be evaluated based on this input interpolation.


Outputs
-------

- **Value** - The value after remapping

Advanced Node Settings
----------------------

- N/A

Note
----

- If the input value is outside the original interval, it will be remapped relative to the start and the end of the new interval. That's why the node has an option to **Clamp The Input**.


Warning
-------

**Custom Interpolation** will not work unless **Clamp Input** is enabled, because interpolation operates on normalized scales.

Examples of Usage
-----------------

.. image:: gifs/map_range_node_example.gif
