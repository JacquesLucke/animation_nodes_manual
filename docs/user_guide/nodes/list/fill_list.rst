Fill List
=========

Description
-----------
This node takes an input list and an input integer that defines the length of the
output list. If the length of the output list is larger than the length of the
input list, the empty spaces are filled with the input element. Those empty spaces
can either be to the left of the list or to its right and that's what **Left**
and **Right** options define. Notice that an empty input list or no input list
at all will return a list that has the length of the input length and filled with
the input element. Notice also that a length smaller than the length of the input
list will return the input list without any change.

.. image:: images/fill_list_node.png
   :width: 160pt

Inputs
------

- **List** - An input list.
- **Length** - The length of the output list.
- **Element** - The element used in filling the empty spaces.

Outputs
-------

- **List** - The filled list.

Advanced Node Settings
----------------------

- **Make Element Copies**
    Activate this option to make Animation Nodes copy the element as often as needed.
    (Instead if just reusing the same element multiple times which can lead to problems
    when the list is modified later)

Examples of Usage
-----------------

.. image:: gifs/fill_list_node_example.gif
