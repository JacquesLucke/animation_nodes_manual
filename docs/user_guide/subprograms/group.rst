*****
Group
*****

To create a new group use the search box and type *Group Input*.

  .. image:: images/group_input_node.PNG

This node is the essential part of a group because it gives you access to the
name and description of the subprogram. Optionally a group can also have a output
node. I suggest to use the "Output Node" button in the group input node because
then both nodes will be internally linked together. You can see that because both
nodes have the same color and when you change the name in the input node the label
in the output node will update automatically.

  .. image:: images/group_input_and_output.PNG

Note that a group output node cannot exist alone. If you accidently removed the
input node the execution will stop because you have an invalid node in the tree.

  .. image:: images/invalid_group_output.PNG

To get everything working again you can either remove the node or connect it to
another node network. If you choose the second option you have to press the "Use
Input in Network" button to let the node search for a connected input node.  
