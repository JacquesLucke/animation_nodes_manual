Random Number
=============

The *Random Number* node outputs a pseudo-random floating point number between
the Min and Max values. You can change the generated number by changing the seed value.

There is an additional seed value that can be useful when generating multiple
random numbers for each frame for example.

If multiple random nodes have the same seed value, they will generate the same number.

.. image:: images/random_node_example_1.png

When they have a different seed value, they will generate a different random number (most likely).

.. image:: images/random_node_example_2.png
