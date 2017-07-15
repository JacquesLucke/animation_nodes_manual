.. _number-wiggle:

Number Wiggle
=============

Description
-----------

This node is a 1D perlin noise generator, You can think of it as random numbers that are smoothly connected to each other.

It is a function of variable **Evolution**, Which means every value of the variable **Evolution** has a corresponding value calculated based on the node options and this value is the output of the node.

.. image:: images/number_wiggle_node.png
   :width: 160pt

Inputs
------

- **Seed** - Seed for the random generator, where different seed generate different noise.
- **Evolution** - A float that is the variable of the function wiggle.
- **Speed** - It is the frequency of the noise or the rate of change of the values.
- **Amplitude** - It is the range of the output values in both positive and negative direction, Means if the *Amplitude* is equal to 1, the values will range between -1 and 1.
- **Octaves** - It is the number of levels of details.
- **Persistance** - It is the strength of the details added from *Octaves*

.. image:: gifs/number_wiggle_node_speed.gif
.. image:: gifs/number_wiggle_node_amplitude.gif
.. image:: gifs/number_wiggle_node_octaves.gif
.. image:: gifs/number_wiggle_node_persistance.gif


Outputs
-------

- **Number** - The output of the noise function at the variable **Evolution**.

Advanced Node Settings
----------------------

- N/A

Note
----

The node has an **extra seed** (*Node Seed*) that can be used to differentiate between nodes with the same seed, e.g., When using multiple *Number Wiggle* nodes in a loop while using the index as a seed, you can change the extra seed to get different results from the other nodes.

Animation Nodes automatically change the *Node Seed* when you duplicate or add a new *Number Wiggle* node.

Examples of Usage
-----------------

.. image:: gifs/number_wiggle_node_example.gif
