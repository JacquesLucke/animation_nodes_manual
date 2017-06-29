Lists
*****

Create Lists
============

**Remove Inputs** in advanced node settings became **Remove Unlinked Inputs** which removed inputs if they weren't connected to any other node.

Get List Element
================

Advanced Node Settings was moved to the node itself for easier and faster control. The node can now get multiple elements if given a list of integers that represent their indices (Possibly polygon and edge indices because under the hood, they are integer lists as well.). To do this, check Use Index List button.

.. image:: images/get_list_element.gif

Mask List
=========

This node was newly added and it selectively remove list elements based on a boolean list where if the boolean at the same index was False, the element is removed.

.. image:: images/mask_list.gif

Sort List
=========

Name, Post Distance and Direction options were removed because they can be achieve using other options.

Random List
===========

This node was newly added, it simply returns a list that contain some random elements from the input list. Unlike the multiple option in the Get Random Element node, elements can be repeated and thus the length of the output node can be larger than the input list.

.. image:: images/random_list.png
