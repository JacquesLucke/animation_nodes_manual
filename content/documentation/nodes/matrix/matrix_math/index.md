---
title : Matrix Math
weight : 1
---

## Description

This node allows you to multiply two transformation matrices.
Multiplying transformation matrices gets you a transformation matrix
that will perform both input transformation matrices. So if you
multiplied a rotation matrix by a translation matrix the resultant
matrix is a transformation matrix that performs rotation and then
translation.

Keep in mind that matrix multiplication is non commutative. So order
matters.

![image](matrix_math_node.png)

## Inputs

  - **A** - A transformation matrix.
  - **B** - A transformation matrix.

## Outputs

  - **Result** - The combined transformation matrix.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video matrix_math_node_example.mp4 >}}
