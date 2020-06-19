---
title : Recalculate Normals
weight : 1
---

## Description

This node recalculate the normals of vertices of the input bmesh.

It is often that the created mesh will have zero normals---The magnitude
of the normals is zero---and you will have to recalculate the normals by
using this node.

![image](recalculate_normals_node.png)

## Options

  - **Invert Normals** - If enabled, computed normals will be inverted.

## Inputs

  - **Bmesh** - An Input Bmesh.

## Outputs

  - **Bmesh** - The resulted Bmesh.

## Advanced Node Settings

  - N/A
