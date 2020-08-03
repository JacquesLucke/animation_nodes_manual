---
title : Spline From edges
---

## Description

This node create splines from the edges of a mesh.

## Options

### Spline Per Edge

This method creates a linear poly spline for every input edge, that is, every
edge will represent a linear poly spline that have 2 point which are the
vertices of the edge.

- **Radius Per Vertex** - This option sets the radius per vertex, so the node
  expects a radius list with the same length as the vertices list.
- **Radius Per Edge** - This option sets the radius per edge, so the node
  expects a radius list with the same length as the edge indices list.

### Spline Per Branch

This method tries to minimizes discontinuity by forming splines from branches
instead of edges.

## Inputs

- **Vertices** - A vector list that represent the position of the
    vertices of the edges.
- **Edge Indices** - An Edge Indices list.
- **Radius(radii)** - The radius of the splines or a list of radii of
    the splines based on the selected option.

## Outputs

- **Splines** - The output splines.
