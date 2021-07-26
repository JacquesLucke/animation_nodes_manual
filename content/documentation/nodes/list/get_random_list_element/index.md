---
title : Get Random List Element
---

## Description

This node returns a single or multiple elements from the input list randomly.

## Options

- **Node Seed** - Aside from the *Seed input*, this extra seed parameter enables
  you to get different random elements if the *Seed input* in not free, that is,
  it is dependent on some property that you can't freely control, for instance,
  when using multiple *Get Random List Element* nodes in a loop while using the
  index as a seed, you can change the node seed to get different elements for
  each node. Animation Nodes automatically changes the *Node Seed* when you
  duplicate or add a new *Get Random List Element* node.
- **Selection Type** - Either choose to return a single random element or
  multiple random elements, in which case, the output list can't have a length
  larger than the input list because the node doesn't allow duplicates.

## Inputs

- **Seed** - Seed for the random generator, where different seed
    return different random elements.
- **List** - The input list.
- **Amount** - The number of random elements in the output list. Can't
    be larger than the the length of the input list. (Only in multiple
    option)

## Outputs

- **List** - A list that contains random elements from the input list.
- **Indices** - The indices of the elements that were chosen from the list.
