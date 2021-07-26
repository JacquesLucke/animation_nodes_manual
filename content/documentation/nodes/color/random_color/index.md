---
title : Random Color
---

## Description

This node generates a random color or a list of random colors.

## Options

- **Node Seed** - Aside from the *Seed input*, this extra seed parameter enables
  you to get different random colors if the *Seed input* in not free, that is,
  it is dependent on some property that you can't freely control, for instance,
  when using multiple *Random Color* nodes in a loop while using the index as a
  seed, you can change the node seed to get different colors for each node.
  Animation Nodes automatically changes the *Node Seed* when you duplicate or
  add a new *Random Color* node.
- **Create List** - It is the button you see beside the *Node Seed*, if enabled,
  the output will be a list of random colors.

## Inputs

- **Seed** - Seed for the random generator, where different seed generate
  different random color.
- **Count** - The number of random colors to generate. (Only available if
  *Create List* is enabled)

## Outputs

- **Booleans(s)** - A random color or a list of random colors.
