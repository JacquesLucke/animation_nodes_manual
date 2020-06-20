---
title : Viewer
weight : 1
---



Debug nodes are now called viewers.

## Viewer

The Debug, Debug List and Debug Drawer nodes were combined into a single
node called Viewer. It automatically determines whether data should be
drawn inline (single element) or in a box (list, or a long text), and
returns information such as datatype and list length (depending on input
datatypes). The result can also be output to text block or console.

![image](viewer_node.png)

![image](viewer_output_settings.png)

## 3D Viewer

This newly added node draws point an empty like objects in the 3D
viewport. If vector(s) were given, then points are drawn in their
locations. If matrices were given, then empty like objects are drawn to
show their orientation as well as their location.

![image](3d_viewer.png)
