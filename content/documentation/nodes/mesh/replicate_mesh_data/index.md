---
title : Replicate Mesh Data
weight : 1
---

## Description

This node copy the input mesh data multiple times then transforms each
new copy based on a corresponding transformation matrix or a translation
vector then copied are combined into a single mesh data. The
transformations are input as a list of matrices or vectors where its
length is the number of copies.

![image](replicate_mesh_data_node.png)

## Options

The transformations can either be defined by matrices which support
translation, rotation and scaling or by vectors that only support
translations.

- **Matrices** - This option lets you define the transformations using
    a transformation matrix list.
- **Vectors** - This option lets you define the translations using a
    vector list.

## Inputs

- **Mesh Data** - The mesh data.
- **Matrices** - A list of transformation matrices that defines the
    transformations applied on the copies where the first matrix is
    applied on the first copy, second on second and so on.
- **Vectors** - A list of vectors that defines the translations
    applied on the copies where the first translation is applied on the
    first copy, second on second and so on.

## Outputs

- **Mesh Data** - A mesh data that contains the copies.

## Advanced Node Settings

- N/A

## Examples of Usage

{{< video replicate_mesh_data_node_example.mp4 >}}
