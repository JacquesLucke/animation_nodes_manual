Boolean To Integer
==================

Description
-----------
This node returns 1 if the input is ``True`` and 0 if the input is ``False``.

.. image:: images/boolean_to_integer_node.png
   :width: 160pt

Demonstration
-------------

The true form of booleans is a binary where 1 means ``True`` and 0 means ``False``.
The logical gates itself is just a simple arithmetical operation on those binaries.
e.g. an *And* gate is just a multiplication and *Or* gate is just an addition clamped to 1.
This node is just a converter that convert booleans into binaries.

Inputs
------

- **Boolean** - An input boolean.

Outputs
-------

- **Number** - The binary.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/boolean_to_integer_node_example.gif
