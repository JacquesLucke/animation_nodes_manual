Character Properties Output
===========================

Description
-----------
This node control the property of the input text object in a specific character interval.

.. image:: images/character_properties_output_node.png
   :width: 160pt

Inputs
------

- **Object** - A text object to edit.
- **Start** - The index of the character when the interval start.
- **End** - The index of the character when the interval end.
- **Material Index** - The index of the material starting from 0.
- **Bold** - Enable or disable bold property.
- **Italic** - Enable or disable italic property.
- **Underline** - Enable or disable underline property.
- **Small Caps** - Enable or disable small caps property.

Outputs
-------

- **Object** - The input object.

Advanced Node Settings
----------------------

- **Allow negative index**
    This option will allow you to invert the interval by entering negative
    values for the start and end indicies.

Examples of Usage
-----------------

.. image:: gifs/character_properties_output_node_example.gif
