---
title : Triangulate BMesh
weight : 1
---

## Description

This node takes a bmesh data type and return a triangulated version of
it.

![image](triangulate_bmesh_node.png)

## Inputs

  - **BMesh** - A bmesh to triangulate.

## Outputs

  - **BMesh** - The triangulated bmesh.

## Advanced Node Settings

  - **Quad Method** - An integer that ranges between 0 and 3, it define
    the method used to perform triangulation of quads.
  - **Ngon Method** - An integer that is either 0 or 1, it define the
    method used to perform triangulation of Ngons.

## Examples of Usage

{{< video triangulate_bmesh_node_example.mp4 >}}
