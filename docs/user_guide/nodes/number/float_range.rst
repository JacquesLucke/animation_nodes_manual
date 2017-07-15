Float Range
===========

Description
-----------

This node is used to generate a float list that represents an arithmetic sequence.

.. image:: images/float_range_node.png
   :width: 160pt

Options
-------

- **Start/Step** - This option allow you to define the arithmetic sequence by a starting value and *Step* value which is the difference between each two consecutive terms.
- **Start/Stop** - This option allow you to define the arithmetic sequence by a starting value and an end value. In this case, the difference between each two consecutive terms is the reciprocal of the *Stop* value.

Inputs
------

- **Amount** - The length of the arithmetic sequence which is also the length of the output integer list.
- **Start** - It is the starting value of the arithmetic sequence.
- **Step** - It is the difference between each two consecutive terms of the arithmetic sequence. (Only available in the *Start/Step* option)
- **Stop** - It is the end value of the arithmetic sequence, in this case, the difference between each two consecutive terms is the reciprocal of its value. (Only available in the *Start/Stop* option)

Outputs
-------

- **Float List** - A float list that contains the generated floats.

Advanced Node Settings
-----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/float_range_node_example.gif
