---
title : Introduction
weight : 10
---

## Add-on

Create a directory with your add-on's name prefixed by `an_`, that is,
`an_<your_extension_name>`. The directory should follow the following base
structure:

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

Do not use `animation_nodes` in your extension name.

{{% / notice %}}

We will explain what needs to be added in those files in a moment. The
`auto_load.py` file can be copied from the Animation Nodes [source][an_source]
without any changes. This file will help us automatically register and load
classes, so it is not mandatory, but it is recommended. For auto loading to
work, each of the directories that have files that define a Blender class needs
to have an empty `__init__.py` file, which are the files you see in the
sub-directories above.

This structure works for simple extensions. More complex extensions that
utilize Cython should follow a more complex structure. This structure is
described later in the Cython [section](#cython).

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
    "version": (1, 0, 0),
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
as we mentioned before. Check the [Node Development][node_dev] guide for
information on how to create nodes or check the Animation Nodes source for
examples on how to write nodes.

### Notes

#### Absolute Imports

In the Animation Nodes source, Animation Nodes objects are imported relatively.
This will not work for extensions. You have to import objects absolutely from
the `animation_nodes` module. So if you see an import statement like this in
the Animation Nodes source:

```python
from .. perlin_noise cimport perlinNoise1D
```

It should be translated into:

```python
from animation_nodes.algorithms.perlin_noise cimport perlinNoise1D
```

#### Extension Module In Execution Code

You can use the `animation_nodes` module—which is also aliased to `AN`—in the
execution code of the node. That's because it is imported by default. In order
to use your extension module, you have to tell Animation Nodes to import it by
overriding the `getUsedModules` method. So the code should be:

```python
    def getUsedModules(self):
            return ["an_<your_extension_name>"]
```

## UI

In order to add your nodes to a menu. In a `node_menu.py` file in the `ui`
directory, define a draw function that either draw other menus or draw node
insert operators directly. Then, in the register function, append this draw
function to any of the Animation Nodes menus or the Add menu directly. For
instance, the following file defines a new menu and draws a node insert
operator in it. Then, a draw function is defined that draws this menu, which is
then appended to the `NODE_MT_add` menu, which is the node add menu. The menu
will be positioned at the end of the menu you appended to.

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

If you would like to write your own Cython code and define your own Cython
structures, you can use the setup script from Animation Nodes, in which case,
your project should follow the following base structure:

```txt
an_<your_extension_name>/
├── setup.py
├── _export_c_setup.py
├── conf.default.json
├── an_<your_extension_name>/
│   ├── ...
├── _setuputils/
│   ├── ...
```

The inner `an_<your_extension_name>` directory is the one illustrated above.
The `_setuputils` directory, `setup.py`, `_export_c_setup.py`, and
`conf.default.json` should be copied from the Animation Nodes
[source][an_source]. The only change you need to make is to change the
`addonName` variable to `an_<your_extension_name>` in both the `setup.py` and
the `_export_c_setup.py` files. The last thing that need to be done is to setup
the headers.

#### Header Files

In order to build your extension, Cython needs to look at the header files of
Animation Nodes. So first download the latest `animation_nodes_headers.zip`
archive from the [release page][latest_release_page], extract it, and configure
the build system to find it by adding the path of the extracted directory to
the array entry named `Cython Include Paths` in the `conf.json` file. Notice
that this file is generated after the first time you build, but you can add it
yourself to the root directory before that. An example `conf.json` is shown:

```json
{
    "Copy Target" : "/path/to/your/blender/addon/directory",
    "Cython Include Paths" : ["/path/to/the/extracted/directory/animation_nodes_headers/"]
}
```

[an_source]: https://github.com/JacquesLucke/animation_nodes
[node_dev]: {{< ref "node_development">}}
[node_menu]: https://github.com/JacquesLucke/animation_nodes/blob/master/animation_nodes/ui/node_menu.py
[latest_release_page]: https://github.com/JacquesLucke/animation_nodes/releases/tag/master-cd-build
