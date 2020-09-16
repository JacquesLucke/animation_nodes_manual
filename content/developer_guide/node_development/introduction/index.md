---
title : Introduction
weight : 10
---

Welcome to this introduction into node development in Animation Nodes
2.0 or higher. In this guide you will learn how to get started with
writing your own nodes (and I suggest you learn this before you try to
modify existing nodes!). It will consist of multiple parts. Each part
will go a bit more into detail so that you will be able to write more
complex nodes in the end. The following tutorials expect you to have a
basic knowledge in Python.

Now you are ready to create the actual file. Since Animation Nodes 2.0
there are two different types of source code files:

- Python files: `.py`  These are just normal python files. Most nodes should be
  of this type, there are only a very few nodes which aren't. I suggest to
  choose this type always at this stage. It will be easy to change it later if
  necessary.

- [Cython](https://www.cython.org/) files: `.pyx` Cython is another programming
  language that builds on top of Python. The main benefit is that it can be
  compiled into machine code which can make it much faster than normal python
  code. For most nodes this is absolute overkill, the performance benefit will
  only be visible be computational expensive operations. Also you can only work
  with Cython files when you setup the complete working environment.

## The First Node

The first simple node we want to create will be able to copy the
location of one object to another object with an offset.

First create a file for this node following the rules above. Then copy
this little template code into the file:

``` python
import bpy
from animation_nodes.base_types import AnimationNode

class TemplateNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TemplateNode"
    bl_label = "Template"

    def create(self):
        pass

    def execute(self):
        pass
```

This template is what I personally use for all new nodes, it is very
easy to build up on it.

Now we have to choose a name for our new node. The most important thing here is
the `bl_idname` because this is the identifier for your node, when you change
it later on, all files that used this node will be broken. Also it should have
a prefix like `an_` so that it there will be no problems with other add-ons. So
make sure that you give it a good name that tells as exact as possible what the
node does. The class name and the `bl_label` property can be changed later
without problems if necessary. Here is the updated "header" for our specific
example:

``` python
class CopyLocationWithOffsetNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_CopyLocationWithOffsetNode"
    bl_label = "Copy Location with Offset"
```

The next step is to create the sockets we need. Therefor there is the
`create(self)` function. In our example node we need three inputs. One
source object, one target object and the offset vector. So let's create
those:

``` python
def create(self):
    #               Type      Name   Identifier
    self.newInput("Object", "Source", "source")
    self.newInput("Object", "Target", "target")
    self.newInput("Vector", "Offset", "offset")
```

When creating a socket, we have to specify at least three parameters:

- Type: This will determine which socket will be created, every socket has a
  different color. There are a lot of socket types. Here are a few common one:
  `Object`, `Vector`, `Float`, `Integer`, `Object List`, ...

- Name: This name will be displayed in the Node Editor in Blender.

- Identifier: The identifier is not very important for us yet. However you it
  shouldn't change if not absolutely necessary, but changing it is not as bad
  as changing the `bl_idname`. It is common to use this identifier as variable
  name in the code later.

Last but not least we have to put some code into the `execute` function.  As
soon as the node has input sockets this function has to have parameters. In
this case we need three parameters, the names should correspond to the socket
identifiers. Also the order has to be the same.  In the function body we can do
whatever we want with these objects. One thing we have to take care of is an
object can be `None`. This has to be checked before anything else happens
because if there is an error in the node, the whole node tree suddenly stops
working.

``` python
def execute(self, source, target, offset):
    if source is None or target is None:
        return

    target.location = source.location + offset
```

This node is already fully functional now. Below is all the code for
this node again.

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

{{< video copy_location_with_offset_1.mp4 >}}

We will continue to work on this node in the next part.
