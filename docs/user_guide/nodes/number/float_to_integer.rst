To Integer
==========

Description
-----------

This node converts floats into integers using one of 3 algorithms. (See advanced node settings)

.. image:: images/to_integer_node.png
   :width: 160pt

Inputs
------

- **Float** - A float to convert to integer.

Outputs
-------

- **Integer** - Output as integer.

Advanced Node Settings
----------------------

The node has 3 algorithms to do the conversion:

- **Floor** - It returns only the whole number.
- **Ceiling** - It returns the next whole number.
- **Round** - Standard round operation, where *floor* is used if the fraction is less than or equal 0.5 and *ceiling* is used if the fraction is larger than 0.5.

+--------+-------+---------+-------+
| Float  | Floor | Ceiling | Round |
+========+=======+=========+=======+
| 0.1    | 0     | 1       | 0     |
+--------+-------+---------+-------+
| 0.6    | 0     | 1       | 1     |
+--------+-------+---------+-------+
| 1.1    | 1     | 2       | 1     |
+--------+-------+---------+-------+
| 1.6    | 1     | 2       | 2     |
+--------+-------+---------+-------+
| 2.1    | 2     | 3       | 2     |
+--------+-------+---------+-------+
