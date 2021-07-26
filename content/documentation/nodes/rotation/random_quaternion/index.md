---
title : Random Quaternion
---

## Description

This node generates a random Quaternion or a list of random Quaternions.

## Options

- **Node Seed** - Aside from the *Seed input*, this extra seed parameter enables
  you to get different random quaternions if the *Seed input* in not free, that
  is, it is dependent on some property that you can't freely control, for
  instance, when using multiple *Random Quaternion* nodes in a loop while using the
  index as a seed, you can change the node seed to get different quaternions for
  each node.  Animation Nodes automatically changes the *Node Seed* when you
  duplicate or add a new *Random Quaternion* node.
- **Create List** - It is the button you see beside the *Node Seed*, if enabled,
  the output will be a list of random quaternions.

## Inputs

- **Seed** - Seed for the random generator, where different seed generates
  different random quaternion.
- **Scale** - Scale of the quaternion elements.
- **Count** - The number of random Quaternions to generate. (Only available if
  *Create List* is enabled)

## Outputs

- **Quaternion(s)** - A random Quaternion or a list of Quaternions.
