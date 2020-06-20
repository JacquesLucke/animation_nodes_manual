---
title : Get Struct List Elements
weight : 1
---

## Description

This node takes a list of structs and output all the values of a
specific common key between them.

If a list of structs all have a key named
<span class="title-ref">Name</span> and you want to output all the texts
in that key, you first have to convert the type of the node to be Text
because Name key is a text and then type
<span class="title-ref">Name</span> in the field.

![image](get_struct_list_elements_node.png)

## Inputs

- **Struct List** - A list of structs.

## Outputs

- **Data** - A list of values based on the type you choosed.

## Advanced Node Settings

- NA

## Examples of Usage

{{< video get_struct_list_elements_node_example.mp4 >}}
