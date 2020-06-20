---
title : Create List
weight : 1
---

## Description

This node is used to create an arbitrary list of a specific data type. A
new element can be added with the *New Input* button. A new element can
also be added by plugging it into the transparent socket. If the list
type is *Object* and no inputs are present, an operator *From Selection*
will be available that adds the currently selected objects as inputs.
See examples.

![image](create_list_node.png)

## Inputs

- **Element** - A element at the index 0.
- **Element** - A element at the index 1.
- **Element** - ...

## Outputs

- **list** - A list that contain all the input data.

## Advanced Node Settings

- **Change type** - Changes the type of the list to another list type.
- **Hide Inputs** - Hides all the inputs in the node.
- **Remove Unlinked Inputs** - Removes all the inputs that are not
    connected to another node.

## Caution

A warning will pop up when you use the *Remove Unlinked Inputs* button
in the node, while if you used the the *Remove Unlinked Inputs* button
in the *Advanced Node Settings* the inputs will be removed without a
warning.

## Examples of Usage

{{< video create_list_node_example.mp4 >}}

{{< video create_object_list_node_example.mp4 >}}
