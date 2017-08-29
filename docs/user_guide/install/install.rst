Installation
************

How to Install?
---------------

0. Uninstall any old version of Animation Nodes. Having it installed multiple times for the same version causes conflicts.

1. Downloaded a recent build for your operating system from `here <https://github.com/JacquesLucke/animation_nodes/releases>`_. If no build suits you, then you might want to compile it yourself (see developers guide) or contact a developer.

2. Open Blender (preferably the newest version)

3. Go to the *User Preferences* in the *Addon* tab.

4. Click *Install from File* and choose the file you downloaded.

5. Activate the add-on and you are **done**.

You can now find the Animation-Nodes editor in the node editor.

    .. image:: images/animation_node_editor.png

.. important::
    Checkout the troubleshooting section below if you have any installation problems.


How to Uninstall?
-----------------

1. Disable the addon and save the user preferences.

2. Restart Blender and remove Animation Nodes.

.. note::
    Animation Nodes must not be active in the session in which it will be removed. This is because some files cannot be removed once they are loaded. This usually is not a problem with other addons because they don't use Cython.

Troubleshooting
---------------

When Animation Nodes fails to start it should show an **error message**. Please read it, often it already contains information on what you can do.

.. image:: images/error_message.png

The addon sometimes depends on features that are only in newer versions of Blender. So the first thing should be to **update** your `Blender <https://www.blender.org/download/>`_ version.

Then make sure that you actually downloaded a build for your operating system (Linux, Windows, macOS and possibly others).

If you use **Windows** try to install `this <https://www.microsoft.com/en-US/download/details.aspx?id=48145>`_ first.

One problem on **Linux** systems is that the builds don't seem to work everywhere. We haven't found a real solution (a build that works everywhere) yet. Therefor we provide multiple Linux builds and you have to check which one works for you.

Animation Nodes depends on `numpy <http://www.numpy.org/>`_. If you downloaded unofficial Blender versions it is possible that *numpy* is not included in those (the error message should tell you this). If this is the case you can either download another Blender build (preferably an `official <https://www.blender.org/download/>`_ one) or you have to install *numpy* manually yourself.

If you still didn't manage to install Animation Nodes you have two options:

    1. Open a `new issue <https://github.com/JacquesLucke/animation_nodes/issues/new>`_ on Github and ask for help. Please provide the relevant data about your computer (OS, Python version, Blender version, ...)
    2. Compile Animation Nodes yourself. You can learn more about that in the developer guide.
