---
title : Create Polygon Indices
weight : 1
---

## Description

This node creates a polygon indices which then can be used to create a
polygon indices list to create meshes.

![image](create_polygon_indices_node.png)

## Options

  -   - **Vertex Amount** - This option generates a polygon indices of a
        specific number of vertices with the sequence `0,1,2,...`.
        
          - **Use list** - It is the option you see beside the menu, if
            enabled, the node will expect a list of vertices amounts and
            the output will be a polygon indices list that include
            polygon indices of corresponding vertices amounts with the
            sequence `0,1,2,...`.

  - **Indices** - This options convert an integer list to a polygon
    indices list.

## Inputs

  - **Indices** - An integer list that contain all the indices of the
    vertices that form the polygon. (Only available in Indices option)
  - **Vertex amount(s)** - The amount of vertices of the polygon, if
    this input was 3, the output polygon indices will be `0,1,2`. (Only
    available in Vertex Amount option)

## Outputs

  - **Polygon Indices** - The resulted polygon indices.

## Advanced Node Settings

  - N/A

## Examples of Usage

{{< video create_polygon_indices_node_example.mp4 >}}
