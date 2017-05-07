Map Range
=========

Description
-----------

This node remaps a value from a defined interval to a new interval.

Every value has a relative position in a specific interval, this node find a new value that match the relative position but in a new defined interval.

.. image:: images/map_range_node.png
   :width: 160pt

Options
-------

- **Clamp** - If enabled, values will be clamped to the interval ``[0,1]``.
- **Interpolation** - If enabled, values will be evaluated at the input interpolation before being output. (Only available when clamp is enabled, as interpolations work on normalized intervals only)

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

Examples of Usage
-----------------

.. image:: gifs/map_range_node_example.gif
