Set List Element
================

Description
-----------
This node replace the value of the element at the input index by the input value.

.. image:: images/set_list_element_node.png
   :width: 160pt

Inputs
------

- **List** - An input list.
- **Index** - The index of the element to change.
- **Element** - The new value.

Outputs
-------

- **List** - The edited list.

Advanced Node Settings
-----------------------

- **Clamp Index**
    If enabled will change the first element for negative input indicies or the
    largest index if the input index is larger than the largest index.

- **Allow Negative Indicies**
    If enabled and clamp is disables, -1 change the last element, -2 change the second last index, ...

Examples of Usage
-----------------

.. image:: gifs/set_list_element_node_example.gif
