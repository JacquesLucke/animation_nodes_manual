Installation
************

How to Install?
---------------

0. Deinstall any old version of Animation Nodes. Having it installed multiple times for the same version causes conflicts.

1. Downloaded a recent build from `Graphics All <http://graphicall.org/blender/?keywords=Animation+Nodes>`_. The build have to match your operating system and python version in order to work. If no build suits you, then you might want to compile it yourself (see developers guide) or contact a developer.

2. Open Blender (preferably the newest version)

3. Go to the *User Preferences* in the *Addon* tab.

4. Click *Install from File* and choose the zip file.

5. Activate the add-on and you are **done**!

You can now find the Animation-Nodes editor in the node editor.
    .. image:: animation_node_editor.png


How to Deinstall?
-----------------

1. Disable the addon and save the user preferences.

2. Restart Blender and remove Blender.

.. note::
    Animation Nodes must not be active in the session in which it will be removed. This is because some files cannot be removed once they are loaded. This usually is not a problem with other addons because they don't use Cython.

Troubleshooting
---------------

The addon sometimes depends on features that are only in newer versions of Blender. So the first thing should be to update your Blender version.

Possible solutions to installation problems:
    * Make sure you downloaded a build for your operating system.
    * Ensure that there is no older version of Animation Nodes installed.
    * If you use Windows, try to install `this <https://www.microsoft.com/en-US/download/details.aspx?id=48145>`_ first.
    * AN depends on the module *numpy* that is distributed with official releases of Blender. If you build Blender yourself or use custom builds (e.g. from graphicall.org) you have to make sure that they contain numpy. If not you have to get another Blender build or install `numpy`_ manually.
    * Enable ``Auto Run Python Scripts`` in the *User Preferences > File* tab.

.. _numpy: http://www.numpy.org/
