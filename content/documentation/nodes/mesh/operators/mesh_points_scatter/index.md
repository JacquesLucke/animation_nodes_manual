---
title : Mesh Points Scatter
weight : 30
---

## Description

This node scatters random points on a mesh surface based on weight.

## Options

- **Node Seed** - Side from the *Seed input*, this extra seed
    parameter enables you to get different random vectors if the *Seed
    input* in not free, that is, it is dependent on some property that
    you can't freely control, for instance, when using multiple *Random
    Vector* nodes in a loop while using the index as a seed, you can
    change the node seed to get different vectors for each node.
    Animation Nodes automatically changes the *Node Seed* when you
    duplicate or add a new *Random Vector* node.

- **Mode** -
    - *Edges* - This allows to scatter points on the edges of a mesh.
    - *Polygons* - This allows to scatter points on the polygons of a mesh.

## Inputs

- **Mesh** - The mesh.
- **Seed** - A integer that specify the seed for random points.
- **Amount** - A integer that specify the amount of random points on the mesh surface.
- **Weights** - A float list of weight *(vertex weight, falloff strength, etc)* can control the scattering of points on the mesh surface.

## Outputs

- **Matrices** - A matrix list that contains the matrices of random points.
- **Vectors** - A vector list that contains the positions of random points.
- **Normals** - A vector list that contains the normals of random points.

## Advanced Settings

- **Use Advanced Method for mesh sampling** - This option allows to use *Ear Clip* method to triangulate mesh for mesh sampling.
