Mix floats
==========

Description
-----------
This node mixes between 2 floats by a defined factor.

.. image:: images/mix_floats_node.png
   :width: 160pt

Inputs
------

- **Factor** - A float that control the amount of each float input to the output, Where 0 means the first float only and 1 means the second float only.


Outputs
-------

- **Result** - The result of mixing the two floats by the factor.

Advanced Node Settings
----------------------

- N/A

Note
----

By how the *Mix floats* works, A factor that is larger than 1 won't be clamped but rather multiplied to the second float- that's why the node has an option to *Clamp Factor*. So if *Clamp factor* is enabled, any factor that is larger than 1 will return the second float.

Examples of Usage
-----------------

.. image:: gifs/mix_floats_node_example.gif
