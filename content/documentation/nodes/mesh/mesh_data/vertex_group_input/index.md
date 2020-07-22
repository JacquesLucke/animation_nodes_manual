---
title : Vertex Group Input
weight : 10
---

## Description

This node returns the weight(s) of the vertices in vertex groups.

## Options

- **All** - The output will be a float list that contain all the
    weights of the chosen vertex group.
- **Index** - The output will be a single float that contain the
    weight of the vertex at the input index.

## Inputs

- **Object** - The object.
- **Group Index** - The index of the vertex group. (See Advanced Node
    Settings)
- **Index** - The Index of the vertex to sample its weight. (Only in
    Index option)
- **Use Modifiers** - If enabled, the values of the weights will be
    sampled after modifiers are applied. (Only in All option)

## Outputs

- **Weight(s)** - A float or a float list of the vertex weight.
