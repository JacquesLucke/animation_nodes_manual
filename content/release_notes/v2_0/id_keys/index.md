---
title : ID Keys
weight : 1
---



An ID Key allows to store custom values on a per object basis. The Id
Keys system got a major update.

Until now there was only one ID Key by default (Initial Transforms). Now
there is a second one (Index) which can be used for all kinds of things.
E.g. it can be used to sort objects before passing them to Animation
Nodes. There are a couple of operators that help with that.

It is possible to create a new ID Key now. Note that it might disappear
after a restart when it is not used anywhere. Furthermore some ID Keys
can be removed as well. Wether a ID Key can be removed depends on where
it is used. It cannot be removed when a Object ID Key node uses it or
when it is one of the default id keys.

Animation Nodes currently supports 4 different types of ID Keys:
Transforms, Text, Float and Integer. All of these can be accessed using
the Object Id Key node.

{{< video id_name.mp4 >}}

## Generating Index ID Keys

Similar to how Transforms ID Keys can be loaded from the current
transforms of an object, integer ID Keys can be generated in multiple
ways.

### Selection Order Method

{{< video selection_order_id.mp4 >}}

### Random Method

{{< video random_sort_id.mp4 >}}

#### Distance Method

{{< video point_distance_id.mp4 >}}

### Axis Method

{{< video axis_sort_id.mp4 >}}

Other options includes alphabetical sorting of object.
