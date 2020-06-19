---
title : Search List Element
weight : 1
---

## Description

This node searches for a specific element and returns some information
about it.

![image](search_list_element_node.png)

## Inputs

  - **List** - The input list.
  - **Search** - A value to search for. This value being of the same
    data type as the input list.

## Outputs

  - **First Index** - The index where the value first appeared in the
    list. So if the input list is `[1,2,3,2]` and we are searching for 2
    then the First Index will be 1 because this is the index where the
    number 2 first appeared.
  - **All Indicies** - A list of the indicies where the search value
    appeared. So using the example above the output will be `[1,3]`
    because the number 2 appeared at both these indicies.
  - **Occurrences** - The number of times the search value appeared on
    the list. So for the example above, the output will be 2 because
    number 2 appeared 2 times in the list.

## Advanced Node Settings

  - **Change type** - Change the type of the list to another list type.

## Examples of Usage

{{< video search_list_element_node_example.mp4 >}}
