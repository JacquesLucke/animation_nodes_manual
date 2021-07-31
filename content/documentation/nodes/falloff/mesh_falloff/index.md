---
title : Mesh Falloff
---

## Description

This node constructs a mesh-based falloff where the falloff value is the distance from the mesh surface.

## Inputs

- **BVHTree** - The BVHTree or an mesh object.
- **Size** - A float value which allows to change the size of the falloff.
- **Falloff Width** - The distance between the ones and the zeroes, can be
    thought of as the slop as well.
- **Fill Inside** - A boolean input allows to make the falloff one inside the mesh.

## Outputs

- **Falloff** - The output falloff.
