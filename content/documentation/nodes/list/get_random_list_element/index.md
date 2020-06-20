---
title : Get Random List Element
weight : 1
---

## Description

This node returns single or multiple elements from the input list
randomly.

![image](get_random_list_element_node.png)

## Options

- **Single** - Returns a single random element.
- **Multiple** - Returns multiple random elements. The output list
    can't have a length larger than the input list because the node
    doesn't allow duplicates.

## Inputs

- **Seed** - Seed for the random generator, where different seed
    return different random elements.
- **List** - The input list.
- **Amount** - The number of random elements in the output list. Can't
    be larger than the the length of the input list. (Only in multiple
    option)

## Outputs

- **List** - A list that contains random elements from the input list.

## Advanced Node Settings

- N/A

## Note

The node has an **extra seed** (*Node Seed*) that can be used to
differentiate between nodes with the same seed, e.g., When using
multiple *Get Random List Element* nodes in a loop while using the index
as a seed, you can change the extra seed to get different results from
the other nodes.

Animation Nodes automatically changes the *Node Seed* when you duplicate
or add a new *Get Random List Element* node.

## Examples of Usage

{{< video get_random_list_element_node_example.mp4 >}}
