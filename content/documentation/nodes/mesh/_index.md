---
title : Mesh
weight : 10
chapter : true
---

# Mesh

### Data Types

- **Mesh** - A data structure that represents a mesh. Mainly, it stores vertices locations and
    possibly edge indices and polygon indices. Additionally, it may store custom data layers
    such as UVs and vertex colors.
- **BMesh** - A data structure that represents a bmesh. It is like mesh, stores vertices locations,
    edge indices and polygon indices but allows to do certain mesh processes e.g., recalculating normals,
    remove doubles, etc.
- **Edge Indices** - A data structure that represents an edge. It is a tuple containing
    two integers.
- **Polygon Indices** - A data structure that represents a polygon. It is a tuple containing
    at least three integers.

### Sockets

- **Mesh Socket** - It can intake or output the mesh(es). This socket has *node link conversion*
    for mesh to vertices and bmesh.
- **BMesh Socket** - It can intake or output the bmesh(es).
- **Edge Indices Socket** - It can intake or output the edge indices (list).
- **Polygon Indices Socket** - It can intake or output the polygon indices (list). This socket
    has *node link conversion* for polygon indices list to edge indices list.

### Nodes

{{% children depth="3" %}}
