---
title : Remap Falloff
weight : 1
---

## Description

This node remaps the floats of the input falloff to a new range. The
node assume that the original range was `[0,1]` Which is usually the
case.

![image](remap_falloff_node.png)

## Inputs

- **Falloff** - A falloff.
- **New min** - The new minimum value.
- **New max** - The new maximum value.

## Outputs

- **Falloff** - The actual falloff object.

## Advanced Node Settings

- N/A

## Examples of Usage

{{< video remap_falloff_node_example.mp4 >}}
