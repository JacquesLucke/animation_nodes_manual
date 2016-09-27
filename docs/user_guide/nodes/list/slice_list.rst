Slice List
==========

Description
-----------
This node output only a portion of the input list.The type of the node change
automatically to whatever the data type you input.

.. image:: images/slice_list_node.png
   :width: 160pt

Options
-------

- **Start,End and Step**
    **Start** define the start index of the output list.So if the input list is
    [1,2,3,4] and Start value is 2 then the new list will be [3,4] thats
    because the node will reject the elements before that index and output a list
    that start from that index.

    **End** in the other hand define the ending index of the output list.
    So assuming the start is 0 and end is 2 the output list will be [1,2,3]
    thats because the node will reject the elements after that index and output a
    list that end by that index.

    **Step** define the step size between every index. So if the step size is
    equal to 2 then the output list will be [1,3] notice that the index jumped
    2 values to get from 1 to 3 and that what the step size define.

- **End Vs Length**
    As explained above, the **End** define the ending index.
    **Length** on the other hand defines the index starting from the start value.
    In other words, the length is the length of the output list that start by the **Start** value.

Inputs
------

- **List** - An input list.
- **Start** - The starting index of the output lengh.
- **End/Lengh** - The ending index or the length of the output list. (Based on the choosen option)
- **Step** - The step size of the output list.

Outputs
-------

- **List** - The sliced list.

Advanced Node Settings
-----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/slice_list_node_example.gif
