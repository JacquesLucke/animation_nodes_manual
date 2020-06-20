---
title : Objects
weight : 1
---



## Object Transforms Output

The Object Transforms Output node has a new UI for enabling
transformation channels. The node now supports editing the delta
transforms of object. Delta transforms are transforms that are added on
top of the current transforms. So now you can define objects relative
transforms without any ID keys. If you want to change the delta
transforms you have to enable this option in the advanced settings. The
node is also vectorized, so you may edit delta transforms for multiple
objects.

{{< video transforms_output.mp4 >}}

## Object Attribute Input

The node now has an operator to create an execution trigger for the
property at the input path ID.

{{< video attribute_input.mp4 >}}

## Object Attribute Output

The node is now vectorized and can take a list of object. When the input
is a list of object, thee **Multiple Values** option appears. Now you
have two options. To set the input value to all object or to provide a
list of values to be set to objects element wise.

{{< video attribute_output.mp4 >}}

## Object Data Path Output

Has a new cache to allow faster execution. The cache can be cleared from
the advanced settings.

## Armature Info

This node was newly added and it gives access to some information about
bones of the input armature like their centers, transformation matrix,
directions, lengths, tails, heads and more.

{{< video armature_info.mp4 >}}

## Object Instancer

The object instancer node now have an option to hide the source object.

{{< video object_instancer.mp4 >}}
