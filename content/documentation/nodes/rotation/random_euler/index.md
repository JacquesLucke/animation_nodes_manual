---
title : Random Euler
---

## Description

This node generates a random Euler or a list of random Eulers.

## Options

- **Node Seed** - Aside from the *Seed input*, this extra seed parameter enables
  you to get different random Eulers if the *Seed input* in not free, that is,
  it is dependent on some property that you can't freely control, for instance,
  when using multiple *Random Euler* nodes in a loop while using the index as a
  seed, you can change the node seed to get different Eulers for each node.
  Animation Nodes automatically changes the *Node Seed* when you duplicate or
  add a new *Random Euler* node.
- **Create List** - It is the button you see beside the *Node Seed*, if enabled,
  the output will be a list of random Eulers.

## Inputs

- **Seed** - Seed for the random generator, where different seed generates
  different random Euler.
- **Scale** - The range in positive and negative directions in radian.
- **Count** - The number of random Eulers to generate. (Only available if
  *Create List* is enabled)

## Outputs

- **Euler** - A random Euler or a list of Eulers.
