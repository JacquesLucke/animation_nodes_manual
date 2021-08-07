---
title : Object Attribute Input
---

## Description

This node returns a specific object property based on the input Data Path of the
property.

To get the data path of any object property in blender, just right click on the
property and click *Copy Data Path*.

## Inputs

- **Object** - An object.

## Outputs

- **Value** - The output value.

## Advanced Node Settings

- **Evaluate Object** - If true, Evaluate the object at the active depsgraph.
  Evaluating the object increases execution time but takes into consideration
  animations, relations, drivers, and so on.
- **Create Execution Trigger** - Create an execution trigger for the selected
  property.
