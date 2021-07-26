---
title : Random Boolean
---

## Description

This node generates a random boolean or a list of random booleans.

## Options

- **Node Seed** - Aside from the *Seed input*, this extra seed parameter enables
  you to get different random booleans if the *Seed input* in not free, that is,
  it is dependent on some property that you can't freely control, for instance,
  when using multiple *Random Boolean* nodes in a loop while using the index as a
  seed, you can change the node seed to get different booleans for each node.
  Animation Nodes automatically changes the *Node Seed* when you duplicate or
  add a new *Random Boolean* node.
- **Create List** - It is the button you see beside the *Node Seed*, if enabled,
  the output will be a list of random booleans.

## Inputs

- **Seed** - Seed for the random generator, where different seed generate
  different random boolean.
- **Probability** - The probability that the boolean will be true.
- **Count** - The number of random booleans to generate. (Only available if
  *Create List* is enabled)

## Outputs

- **Booleans(s)** - A random boolean or a list of random booleans.
