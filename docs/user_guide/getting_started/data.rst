****
Data
****

There are multiple data types in Animation Nodes, ones that mathematical like integers, floats, vectors and quaternions and ones that represent a data structure like BVH trees, mesh data and KD trees. Most of the data types have their own list data type. So integers have integers lists, vectors have vector lists and so on.

Copying Data
============

Animation Nodes automatically copy data if needed. For example, if you have a list of vectors and you input it to a single shuffl node, the data don't need to be copied and the original list is shuffled. If however I input it to another shuffle node, the data has to be copied because two nodes are using it, if it wasn't copied, then the second node will shuffle the shuffled list and not the list itself.

Animation Nodes have an option to identify nodes that copy data, you can enable by chaning **Color Mode** to *Needed Copies* in the developer panel.

.. image:: images/color_copies.png

Notice that objects are the only data that should be copied, simple data types like integers and floats are just bits and are copied automatically when operated on. Some other data types can not be copied, but this isn't really essential for you to know.

Generic Data Type
=================

Sometimes there isn't a data type that may suite your need, so it can be stored in what is known as the generic data type. For instance, nested lists, that is, a list of lists can not be stored in any of the available data types, so we store them in a generic data type.

However, when using generic data types in a node, they have to be converted back to a data type AN knows, for instance, if we have a list of float lists, getting the first list of the this generic list would return a generic data type and not a float list, if I want to get the first float in the output list, I have to convert it to an AN float list first, this can be done using the converter node:

.. image:: images/converter_node.png

Notice that I could have get the element as generic element then convert it to a float at the end, and it would have worked just the same.

Convert Node
------------

The converter node convert and data type to any other data type if possible, the node automatically detect input and outputs, so if you want it to stope changing types, you have to chekc the lock button and choose the tpe mmanually by pressing on the only button there.
