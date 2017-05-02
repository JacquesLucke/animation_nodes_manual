String List
===========

Description
-----------

This node is used to create an arbitrary list of strings. A new string can be added with the *New Input* button. A new string can also be added by plugging it into the transparent socket.

.. image:: images/string_list_node.png
   :width: 160pt

Inputs
------

- **String** - A string at the index 0.
- **String** - A string at the index 1.
- **String** - ...

Outputs
-------
- **String list** - A list that contains all the input strings.

Advanced Node Settings
-----------------------

- **Change type** - Change the type of the string list to another list type.
- **Hide Inputs** - Hide all the inputs in the node.
- **Remove Unlinked Inputs** - Removes all the inputs that are not connected to another node.

Caution
-------

A warning will pop up when you use the *Remove Unlinked Inputs* button in the node, while if you used the the *Remove Unlinked Inputs* button in the *Advanced Node Settings* the inputs will be removed without a warning.

Examples of Usage
-----------------

.. image:: gifs/string_list_node_example.gif
