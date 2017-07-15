Get Struct Elements
===================

Description
-----------

This node is used to get a value from a struct.

.. image:: images/get_struct_elements_node.png
   :width: 160pt

Demonstration
-------------

This node doesn't output all the values of the struct, you have to request what you want. Using the example we used in the :ref:`set_struct` page. If we want to get the name of the person, we should add a string output and type "Name" which is the key that store the name of the person.

Getting such value in animation nodes :

.. image:: images/get_struct_elements_node_example_1.png

Inputs
------

- **Struct** - The input struct.

Outputs
-------

Based on what you add.

Advanced Node Settings
----------------------

- **Make Copies** - Copy the element before outputting it. This makes sure the element is independent of the original element in the struct and so changing that element won't affect the output.

Examples of Usage
-----------------

.. image:: gifs/get_struct_elements_node_example_2.gif
