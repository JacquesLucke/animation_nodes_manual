Mix Vectors
===========

Description
-----------
This node mix between 2 eulers by a defined factor.

.. image:: images/mix_euler_node.png
   :width: 160pt

Inputs
------

- **Factor** - A float that control the amount of each euler input to the output, Where 0 means the first euler only and 1 means the second euler only.


Outputs
-------

- **Result** - The result euler of mixing the two eulers by the input factor.

Advanced Node Settings
----------------------

- N/A

Note
----

By how the *Mix Eulers* works, A factor that is larger than 1 won't be clamped but rather multiplied to the second euler, That's why the node has an option to *Clamp Factor*. So if *Clamp factor* is enables, Any factor that is larger than 1 will resturn the second euler.

Examples of Usage
-----------------

.. image:: gifs/mix_euler_node_example.gif
