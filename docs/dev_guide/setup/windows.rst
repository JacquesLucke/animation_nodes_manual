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
    Clone the repository to your local hard drive.

    .. attention::
        The cloning target location used to be the addon folder of Blender.
        This is no longer the case. You can clone it anywhere you want.


    If you are using this guide before the official AN 2.0 release you have to
    switch to the ``cython`` branch. You can do this either by running
    ``git checkout cython`` or by using the GUI you installed.



Compile the Code
****************

1. Install Python
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

2. Install Cython
    When you installed *Anaconda* there is now an command line tool called ``conda``.
    It allows you to easily install other python packages.

    Run ``conda install cython``.

    If you have not used the *Anaconda* package, look here for more information
    on how to install cython: http://cython.readthedocs.io/en/latest/src/quickstart/install.html

3. Run the ``setup.py`` script
    Open the ``setup.py`` file. Inside there is a variable called ``addonsDirectory``
    at the top. You may want to change it to the location of the addons folder
    of your Blender version. This allows the setup script to automatically copy
    the complete build into this folder. Take care that you don't accidently
    commit this change (or at least undo it before making Pull Requests).
    If you know a better solution to this problem, please create an Issue on Github.

    Run ``python setup.py``.

    This can take multiple minutes the first time.
    Take a look into the **Troubleshooting** section if an error occured.

The ``setup.py`` file has a few command line arguments:

    - ``-all``
        This will rebuild all cython files which can be quite useful when
        Cython does not automatically detect all files that need to update
        after you've made a change. Should not be needed in most cases though.
    - ``-export``
        Create an ``animation_nodes.zip`` file that can be shared with others.


Troubleshooting
***************

If your problem is not mentioned here, please
`report <https://github.com/JacquesLucke/animation_nodes_manual/issues/new>`_ it.

unable to find vcvarsall.bat
----------------------------

To fix this you need install Visual Studio 2015 Community, especially
the **Common Tools for Visual C++ 2015** as you can see here:
http://stackoverflow.com/a/35243904/4755171

Installing Visual Studio can take a while, but the problem should disapper afterwards.
