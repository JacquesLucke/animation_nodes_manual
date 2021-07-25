---
title : Shade Object Smooth
weight : 60
---

## Description

This node set the shading of the input object to smooth or flat.

## Inputs

- **Object** - An Object.
- **Smooth** - A boolean which if true will shade the object smooth and if false
  will shade the object flat. The socket has an *Is Used* property, if true the
  node will take effect, otherwise, the node will be disabled and will not take
  effect.

## Outputs

- **Object** - The input object.

## Note

If you shaded an object smooth and it get rendered black, then its
normals are null vectors and you will have to recalculate the normals
using the *Recalculate Normals Node*.
