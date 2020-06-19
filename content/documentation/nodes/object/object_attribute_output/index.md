---
title : Object Attribute Output
weight : 1
---

## Description

This node sets the chosen property to the input value. Custom properties
can also be edited using this node by typing
<span class="title-ref">\["Property Name"\]</span> in the expressions
field, if there was no such csutom property, it will be created.

To get the data path of any object property in blender, just right click
on the property and select **Copy Data Path**.

![image](object_attribute_output_node.png)

## Options

  - **Multiple Values** - If Object list was used as an input, this
    option will be available. If disabled, the input value will be set
    to the property for all objects. If enabled, the input value will
    expect a list of values where each element correspond to the value
    which will be set to the object property of the object at the same
    index.

## Inputs

  - **Object** - An object.
  - **Value** - The value of the property.

## Outputs

  - **Object** - The input object.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video object_attribute_output_node_example.mp4 >}}
