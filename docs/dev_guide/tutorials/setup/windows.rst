Setup Environment on Windows
============================

Download the Source Code
************************

1.
    If you have Animation Nodes already installed, remove it.

2.
    Install  `git <https://git-scm.com/>`_ or a
    `gui client <https://git-scm.com/downloads/guis>`_
    (I use **Github Desktop** all the time).

3.
    Create a `GitHub <https://github.com/>`_ account.

4.
    `Fork <https://guides.github.com/activities/forking/>`_ the addon repository.

5.
    Clone the repository into Blenders addon folder.

    The path should be like this:
    ``C:\Users\#NAME#\AppData\Roaming\Blender Foundation\Blender\2.77\scripts\addons``

    After that there should be a folder called exactly ``animation_nodes`` in
    the ``addons`` folder. It should contain these two files (beside others):
    ``__init__.py`` and ``setup.py``. (If you are using this guide before the
    official AN 2.0 release you have to switch to the ``cython`` branch.
    You can do this either by running ``git checkout cython`` or by using the
    GUI you installed.)

    Blender should now already be able to find the addon but it cannot be activated
    yet because we first need to compile it.


Compile the Code
****************

1.
    Install Python 3.5.x on your system. Older versions are not supported.
    I suggest to install *Anaconda* (which contains Python 3.5.x) because
    it makes installing Cython later much easier.

    Download Anaconda: https://www.continuum.io/downloads

    To test if you are using the right version you can run ``python -V`` in
    any terminal. For me it returns ``Python 3.5.1 :: Anaconda 4.0.0 (64-bit)``,
    different outputs are possible, just make sure that the Python version is correct.

    Sometimes, when you have multiple Python versions installed, you might have
    to run ``python3 -V`` or ``python3.5 -V``. If that is the case, use this
    version later.

2.
    When you installed *Anaconda* there is now an command line tool called ``conda``.
    It allows you to easily install other python packages.

    Run ``conda install cython``.

    If you have not used the *Anaconda* package, look here for more information
    on how to install cython: http://cython.readthedocs.io/en/latest/src/quickstart/install.html

If you are lucky this was it already (in my case it was not..)

To test if everything is setup correctly we can just try to compile AN now.
For that navigate into the ``animation_nodes`` addon folder and open up a
terminal. (In Windows 10 you can hold down shift and right click into the
folder. Holding down shift will show you an extra option to open up a console)

Run this command: ``python setup.py`` (or ``python3`` or whatever you need)

Now it should start to do something. The whole script can take a minute or two
to run. If it runs without problems you're done. You can now start Blender
and activate the addon. If not, checkout the troubleshooting section.

As long as you only change ``.py`` files you don't have to recompile again.


Troubleshooting
***************

If your problem is not mentioned here, please report it here:
https://github.com/JacquesLucke/animation_nodes_manual/issues/new

unable to find vcvarsall.bat
----------------------------

To fix this you need install Visual Studio 2015 Community, especially
the **Common Tools for Visual C++ 2015** as you can see here:
http://stackoverflow.com/a/35243904/4755171

Installing Visual Studio can take a while, but the problem should disapper afterwards.
