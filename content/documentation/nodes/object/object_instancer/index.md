---
title : Object Instancer
---

## Description

This node dynamically creates and duplicates objects.

## Options

- **Copy from source** - This option is enabled by default and it lets you
  instance an object with its data, however, if the option is disabled, the
  node will create objects with empty data blocks which you can then fill and
  control by other nodes like the *Copy Object Data Node* or the *Object
  Output Node*.
- **Object Type** - This option is only visible when *copy from source* is
  disabled. It lets you define the type of data block the object should carry,
  so the data can be *Mesh*, *Curve*, *Lamp*, etc.
- **Copy full object** - If enabled will copy the modifiers and the constraints
  with the object. (Only available when Copy From Source is enabled)
- **Deep copy** - If enabled will copy mesh data as well so that every data
  block has a single user. The new object will be independent of the source.
  (Only available when Copy From Source is enabled)

## Inputs

- **Instances** - The number of instances created of the object.
- **Object** - The input object to instance. (Only available when Copy
    From Source is enabled)

## Outputs

- **Objects** - A list that contains the instanced objects.

## Advanced Node Settings

- **Container Type** -
  - **Main Container** - Add the resulted objects to the Animation Nodes main
    container collection in all input scenes.
  - **Scenes** - Add the resulted objects to the scene collection in all input
    scenes.
  - **Collections** - Add the resulted objects to all input collections.
- **Remove Animation Data** - Clear the animation data of the newly created
  objects.
- **Reset Source Data** - This will reset the source data for all instances.
- **Unlink instances from node** - This will separate the instances from the
  node to make sure they don't get removed when you remove the node.
- **Hide relationship lines** - This will hide the lines going to the container
  in the view-port.
