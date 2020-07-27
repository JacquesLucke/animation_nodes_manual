---
title : Spline
weight : 11
chapter : true
---

# Spline

### Data Types

- **Spline** - A data structure that represents a poly spline and bezier spline. For poly spline,
    it stores points' locations, radii, tilts and cyclic. For bezier spline, it also stores handles'
    locations.

### Sockets

- **Spline Socket** - It can intake or output the spline(s). The spline input socket has two eye droppers, the first eye dropper icon will allow to select curve object from 3D viewport or outliner. The second eye dropper icon (solid) will set the input object to the active curve object in the 3D viewport, and hold CTRL to open a rename object dialog. It also has *World Space* button that converts points to
world space.

### Nodes

{{% children %}}
