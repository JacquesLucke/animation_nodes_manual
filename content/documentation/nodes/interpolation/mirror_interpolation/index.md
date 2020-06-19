---
title : Mirror Interpolation
weight : 1
---

## Description

This node can be used to get the inverse of the input interpolation, the
node can also combine the interpolation with its inverse resulting in a
symmetric function around the line `x=0.5`.

![image](mirror_interpolation_node.png)

## Options

  - **Chain** - If enabled, the interpolation will be combined with its
    inverse, where the original interpolation will be remapped to the
    domain `[0,0.5]` and its inverse in the domain `[0.5,1]`. If
    disabled, the output will be the inverse of the interpolation.

## Inputs

  - **Interpolation** - An interpolation.

## Outputs

  - **Interpolation** - The new interpolation.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video mirror_interpolation_node_example.mp4 >}}
