---
title : Mix Matrices
weight : 1
---

## Description

This node mixes between 2 matrices based on a factor.

![image](mix_matrices_node.png)

## Inputs

- **Factor** - A float that controls the amount of each matrix input
    to the output, where 0 means the first matrix only and 1 means the
    second matrix only.

## Outputs

- **Result** - The resultant matrix of mixing the two matrices by the
    input factor.

## Advanced Node Settings

- N/A

## Note

A factor that is larger than 1 won't be clamped but rather multiplied to
the second matrix. That's why the node has an option to *Clamp Factor*.
So if *Clamp Factor* is enabled, any factor that is larger than 1 will
return the second matrix.

## Examples of Usage

{{< video mix_matrices_node_example.mp4 >}}
