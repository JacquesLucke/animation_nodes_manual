---
title : Replicate GP Layer
weight : 60
---

## Description

This node replicates gp layer(s) based on the input matrices or vectors. This node also allows to set some of the attributes of replicated layers.

## Options

- **Transformation Type** -
    - *Matrices* - This option replicates gp layer(s) based on the matrices.
    - *Vectors* - This option replicates gp layer(s) based on the vectors.

## Inputs

- **Layer(s)** - A gp layer or a gp layer list.
- **Transformations** - A matrix list or A vector list.
- **Offset Frame** - A float or a float list to offset the frame number of frames of replicated gp layers.
- **Tint Color** - A color or a color list to set the tint color of replicated gp layers.
- **Tint Factor** - A float or a float list to set the tint factor of replicated gp layers.
- **Stroke Thickness** - A float or a float list to set the stroke thickness of replicated gp layers.

## Outputs

- **Layers** - A gp layer list.
