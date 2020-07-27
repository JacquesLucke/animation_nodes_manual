---
title : Grease Pencil
weight : 12
chapter : true
---

# Grease Pencil

### Data Types

- **Layer** - A data structure that represents a grease pencil (abbreviated as gp) layer. It
    stores frames, layer name, opacity, blend mode, etc.
- **Frame** - A data structure that represents a gp frame. It stores strokes and
    frame number.
- **Stroke** - A data structure that represents a gp stroke. It stores points'
    location, strength, pressure, vertex color, etc.

### Sockets

- **Layer Socket** - It can intake or output the gp layer(s). This socket has *node link conversion*
    for layer to frame.
- **Frame Socket** - It can intake or output the gp frame(s). This socket has *node link conversion*
    for frame(s) to layer and frame to stroke.
- **Stroke Socket** - It can intake or output the gp stroke(s). This socket has *node link conversion*
    for text block.

### Nodes

{{% children %}}
