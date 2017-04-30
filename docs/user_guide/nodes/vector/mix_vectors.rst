Mix Vectors
===========

Description
-----------

This node mixes between 2 vectors based on a factor.

.. image:: images/mix_vectors_node.png
   :width: 160pt

Inputs
------

- **Factor** - A float that controls the amount of each vector input to the output, Where 0 means the first vector only and 1 means the second vector only.


Outputs
-------

- **Result** - The result vector of mixing the two vectors by the input factor.

Advanced Node Settings
----------------------

- N/A

Note
----

How the *Mix Vectors* works, a factor that is larger than 1 won't be clamped but rather multiplied to the second float- that's why the node has an option to *Clamp Factor*. So if *Clamp factor* is enabled, Any factor that is larger than 1 will return the second vector.

Examples of Usage
-----------------

.. image:: gifs/mix_vectors_node_example.gif
