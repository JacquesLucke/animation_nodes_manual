---
title : Set Vertex Weight
weight : 20
---

## Description

This node sets the weight(s) of the vertices in vertex groups.

## Options

- **All** - The Weight(s) input will be a float list that contain all the
    weights for the choosen vertex group.
- **Index** - The Weight(s) input will be a single float that contain the
    weight for the vertex at the input index.

## Inputs

- **Object** - The object.
- **Group Index** - The index of the vertex group. (See Advanced Node
    Settings)
- **Index** - The Index of the vertex to set its weight. (Only in
    Index option)
- **Weight(s)** - A float or a float list for the vertex weight.

## Outputs

- **Object** - The object.

## Advanced Node Settings

- **Type** -
    - *Index* - This option allows to select the vertex group by the index.
    - *Name* - This option allows to select the vertex group by the name.
