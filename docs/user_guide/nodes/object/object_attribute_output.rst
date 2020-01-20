Object Attribute Output
=======================

Description
-----------

This node sets the chosen property to the input value. Custom properties can also be edited using this node by typing `["Property Name"]` in the expressions field, if there was no such custom property, it will be created.

To get the data path of any object property in blender, just right click on the property and select **Copy Data Path**.

.. image:: images/object_attribute_output_node.png
   :width: 160pt

Options
-------

- **Multiple Values** - If Object list was used as an input, this option will be available. If disabled, the input value will be set to the property for all objects. If enabled, the input value will expect a list of values where each element correspond to the value which will be set to the object property of the object at the same index.

Inputs
------

- **Object** - An object.
- **Value** - The value of the property.

Outputs
-------

- **Object** - The input object.

Advanced Node Settings
----------------------

- N/A

Examples of Usage
-----------------

.. image:: gifs/object_attribute_output_node_example.gif
