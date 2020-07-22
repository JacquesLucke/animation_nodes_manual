---
title : Grease Pencil
---

Newly added grease pencil nodes allows to get and modify grease pencil object data (layers, frames, strokes), and create new grease pencil objects from scratch with nodes. The grease pencil nodes can be divided three categories Input nodes, Output nodes and Modify nodes.

## Input Nodes

There are four input nodes _GP Object Input, GP Layer Info, GP Frame Info,_ and _GP Stroke Info_. These
nodes allows to get the information about the grease pencil object e.g., layers, frames, strokes.

{{< video gp_input_nodes.mp4 >}}

## Output Nodes

There are five input nodes _GP Stroke From Points, GP Stroke From Spline, GP Frame From Strokes, GP
Layer From Frames_, and _GP Material Output_. These nodes allows to create gp object from the input data.

{{< video gp_output_nodes.mp4 >}}

## Modify Nodes

There are eight modify nodes _Set GP Layer Attributes, Replicate GP Layer, Transform GP Layer, Offset
GP Layer Frame, Set GP Stroke Attributes, Replicate GP Stroke, Transform GP Stroke,_ and _Offset
GP Stroke_. These nodes allows to modify the layers and strokes.

{{< video gp_modify_nodes.mp4 >}}
