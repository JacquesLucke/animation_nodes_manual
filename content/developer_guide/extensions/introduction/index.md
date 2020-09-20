---
title : Introduction
weight : 10
---

## Add-on

Create a directory with the prefix `an_` in the name, that is,
`an_<your_extension_name>` with the following base structure:

```txt
an_<your_extension_name>/
├── __init__.py
├── auto_load.py
├── ui/
│   ├── __init__.py
│   ├── node_menu.py
├── nodes/
│   ├── __init__.py
│   ├── ...
```

{{% notice warning %}}

Do not use `animation_nodes` in your extension names.

{{% / notice %}}

We will explain what needs to be added in those files in a moment. The
`auto_load.py` file can be downloaded from [here][auto_load] without any
changes. This file will help us automatically register and load classes, so it
is not mandatory, but it is recommended. For auto loading to work, each of the
directories that have files that define a Blender class needs to have an empty
`__init__.py` file, which are the files you see in the sub-directories above.

## Initialization

In the top-level `__init__.py` file, we need to do two things:

- Make sure Animation Nodes is loaded and available.
- Initialize the automatic loader and register/unregister the classes.

```python
'''
Copyright (C) 2020 <YOUR NAME>
<YOUR EMAIL>

Created by <YOUR NAME>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Animation Nodes Test Extension",
    "author": "<YOUR NAME>",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "Animation Nodes",
    "description": "A Test Extension For Animation Nodes.",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Nodes",
}

import bpy
import addon_utils
from . import auto_load

if not all(addon_utils.check("animation_nodes")):
    module = addon_utils.enable("animation_nodes", default_set = False, persistent = True)
    if not module:
        raise Exception("Could not load Animation Nodes.")

auto_load.init()

def register():
    auto_load.register()
    
def unregister():
    auto_load.unregister()
```

## Nodes

Add your nodes inside the `nodes` directory or any of its sub-directories. The
directory and its sub-directories should each have an empty `__init__.py` file
as we mentioned before. Check the [Node Development]({{< ref "node_development"
>}}) guide for information on how to create nodes or check the Animation Nodes
source for examples on how to write nodes.

## UI

In order to add your nodes to a menu. In a `node_menu.py` file in the `ui`
directory, define a draw function that either draw other menus or draw node
insert operators directly. Then, in the register function, append this draw
function to any of the Animation Nodes menus or the Add menu directly. For
instance, the following file defines a new menu and draws a node insert
operator in it. Then, a draw function is defined that draws this menu, which is
then appended to the `NODE_MT_add` menu, which is the node add menu. The menu
will be positioned at the end of the menu.

```python
import bpy
from animation_nodes.ui.node_menu import insertNode

class TestExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_test_extension_menu"
    bl_label = "Test Extension Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_TestExtensionNode", "Test Extension Node")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    layout.separator()
    layout.menu("AN_MT_test_extension_menu", text = "Test Extension Menu", icon = "SCRIPTPLUGINS")

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
```

Had I wanted to add the menu to the vectors menu in Animation Nodes, I would
have appended to the `AN_MT_vector_menu` menu instead. For a full list of
menus and more examples on how to define more complex menus, check the
`node_menu.py` file in the Animation Nodes source [here][node_menu].

## Cython

You may use any of the public Cython functions defined by Animation Nodes.
However, this guide doesn't cover writing your own Cython code, and we don't
officially release any headers to aid the development of Cython nodes at the
moment.

[auto_load]: https://raw.githubusercontent.com/JacquesLucke/animation_nodes/master/animation_nodes/auto_load.py
[node_menu]: https://github.com/JacquesLucke/animation_nodes/blob/master/animation_nodes/ui/node_menu.py
