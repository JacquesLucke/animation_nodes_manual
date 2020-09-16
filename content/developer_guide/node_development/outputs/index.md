---
title : Outputs
weight : 20
---

In the last part we created our first little node that copies the
location from one object to another object and applies a custom offset.
Here is the result of the last chapter:

``` python
import bpy
from animation_nodes.base_types import AnimationNode

class CopyLocationWithOffsetNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_CopyLocationWithOffsetNode"
    bl_label = "Copy Location with Offset"

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newInput("Object", "Target", "target")
        self.newInput("Vector", "Offset", "offset")

    def execute(self, source, target, offset):
        if source is None or target is None:
            return

        target.location = source.location + offset
```

In this part we want to extend this node. At first we want to change the
node so that it outputs the new location of the target object. Therefor
we need to write a new line in the `create(self)` function like so:

``` python
def create(self):
    self.newInput("Object", "Source", "source")
    self.newInput("Object", "Target", "target")
    self.newInput("Vector", "Offset", "offset")
    self.newOutput("Vector", "Target Location", "targetLocation")
```

Pretty straight forward, right? Now I have to adapt the `execute` method
so that it actually returns a vector. At the moment it just return
`None` all the time. It is very important that `execute` **always**
returns a vector now. All the other the might use this value depend on
this being a vector and don't check the type explicitly. This means that
you should return default values if there is anything wrong in your
node. The new method can look like so:

``` python
def execute(self, source, target, offset):
    if source is None or target is None:
        return Vector((0, 0, 0)) # this is the default value

    target.location = source.location + offset
    return target.location
```

As you can see we create this `Vector((0, 0, 0))` object. Every
individual vector is expected to be this type. In order to make this
code work we need to import the type at the top of the file: `from
mathutils import Vector`.

The node is completely functional now again.

``` python
import bpy
from mathutils import Vector
from animation_nodes.base_types import AnimationNode

class CopyLocationWithOffsetNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_CopyLocationWithOffsetNode"
    bl_label = "Copy Location with Offset"

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newInput("Object", "Target", "target")
        self.newInput("Vector", "Offset", "offset")
        self.newOutput("Vector", "Target Location", "targetLocation")

    def execute(self, source, target, offset):
        if source is None or target is None:
            return Vector((0, 0, 0))

        target.location = source.location + offset
        return target.location
```

{{< video copy_location_with_offset_2.mp4 >}}

Now we want to change the node so that it outputs not only the location
of the target object but also the location of the source object. I guess
at this point it is clear how we have to change the `create(self)`
method.

``` python
def create(self):
    self.newInput("Object", "Source", "source")
    self.newInput("Object", "Target", "target")
    self.newInput("Vector", "Offset", "offset")
    self.newOutput("Vector", "Source Location", "sourceLocation")
    self.newOutput("Vector", "Target Location", "targetLocation")
```

Python has the wonderful feature that you can easily return multiple
objects from a method. To return two objects we will use exactly this
feature. There are two main things you have to know about that:

1. The amount of returned objects always has to match the amount of
   output sockets.
2. The order of the returned objects has to correspond to the order of
   the output sockets.

To fulfill these two requirements the code of the `execute` method can
look like so:

``` python
def execute(self, source, target, offset):
    if source is None or target is None:
        return Vector((0, 0, 0)), Vector((0, 0, 0)) # we need two defaults as well

    target.location = source.location + offset
    return source.location, target.location
```

Again our node is fully functional and so we come to the end of this
part.

``` python
import bpy
from mathutils import Vector
from animation_nodes.base_types import AnimationNode

class CopyLocationWithOffsetNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_CopyLocationWithOffsetNode"
    bl_label = "Copy Location with Offset"

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newInput("Object", "Target", "target")
        self.newInput("Vector", "Offset", "offset")
        self.newOutput("Vector", "Source Location", "sourceLocation")
        self.newOutput("Vector", "Target Location", "targetLocation")

    def execute(self, source, target, offset):
        if source is None or target is None:
            return Vector((0, 0, 0)), Vector((0, 0, 0))

        target.location = source.location + offset
        return source.location, target.location
```

{{< video copy_location_with_offset_3.mp4 >}}
