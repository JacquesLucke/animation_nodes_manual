---
title : Mask List
weight : 1
---

## Description

This node can be used to selectively remove list elements based on a
boolean list. A boolean list with the same length as the input list has
to be provided, for every element in the input list, if the boolean at
the same index in the boolean list was False, then this element will not
be included in the output list.

![image](mask_list_node.png)

## Inputs

  - **List** - An input list.
  - **Mask** - A boolean list.

## Outputs

  - **List** - The output list.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video mask_list_node_example.mp4 >}}
