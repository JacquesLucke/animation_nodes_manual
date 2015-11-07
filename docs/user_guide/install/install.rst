***************
How to Install?
***************


1. Download the zip file at the official repository https://github.com/JacquesLucke/animation_nodes
    .. image:: zip.png

2. Open Blender (preferably the newest version)

3. Go to the *User Preferences* in the *Addon* tab.

4. Click *Install from File* and choose the zip file.

5. Activate the add-on and you are **done**!

You can now find the Animation-Nodes editor in the node editor.
    .. image:: animation_node_editor.png


Troubleshooting
***************

The addon sometimes depends on features that are in newer versions of Blender.
So the first thing should be to update your Blender version.

Possible solutions to installation problems:
    * Enable ``Auto Run Python Scripts`` in the *User Preferences > File* tab.
    * AN depends on the module *numpy* that is distributed with official releases
      of Blender. If you build Blender yourself or use custom builds
      (e.g. from graphicall.org) you have to make sure that they contain numpy.
      If not you have to get another Blender build or install `numpy`_ manually.

.. _numpy: http://www.numpy.org/      
