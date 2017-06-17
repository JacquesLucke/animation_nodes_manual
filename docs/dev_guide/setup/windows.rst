Setup Environment on Windows
============================

Download the Source Code
************************

1.
    If you have Animation Nodes already installed, remove it.

2.
    Install  `git <https://git-scm.com/>`_ and optionally a
    `gui client <https://git-scm.com/downloads/guis>`_
    (I use **Github Desktop** all the time).

3.
    Create a `GitHub <https://github.com/>`_ account.

4.
    `Fork <https://guides.github.com/activities/forking/>`_ the addon repository.

5.
    Clone the repository to your local hard drive.

    .. attention::
        The cloning target location used to be the addon folder of Blender. This is no longer the case. You can clone it anywhere you want.


    If you are using this guide before the official AN 2.0 release you have to switch to the ``cython`` branch. You can do this either by running ``git checkout cython`` or by using the GUI you installed.



Compile the Code
****************

1. Install Python (Anaconda)
    First we have to install Python itself. You should use `Anaconda <https://www.continuum.io/downloads>`_ for that. Just take the newest version.

    Installing Python this way has multiple benefits:
    - easier installation of other packages
    - easier handling of multiple Python environments

    Make sure that Anaconda has been added to the ``PATH`` system environment variable. You can test if the installation worked by running ``python -V`` (in a newly opened terminal window). The output should include ``Continuum Analytics, Inc.`` somewhere.

    Depending on what Blender version you want to compile the addon for, different versions of Python are necessary. All newer Blender versions up until Blender 2.79 officially use Python 3.5.x. The plan is to update to Python 3.6 in the Blender 2.8 project.

    As Animation Nodes currently does not work with Blender 2.8 I guess you want to compile using Python 3.5. What we can do now is to create a Python environment for that version. Fortunately Anaconda makes this fairly easy to set up.

    To create the Python 3.5 environment, just run ``conda create -n py35 python=3.5 anaconda``. The new environment will be called ``py35``. To activate it you need to run ``activate py35`` (or in some terminals ``source activate py35``). When you now run ``python -V`` it should show you that you are using Python 3.5. You have to activate the environment everytime you reopen the terminal. More Information can be found `here <https://conda.io/docs/py2or3.html>`_.

    .. note::
        The following steps should all be executed in the new correct Python environment.

2. Install Cython
    When you used Anaconda, it will be easy to install Cython.

    Just run ``conda install cython``.

3. Build Animation Nodes
    This step is the most error prone, if you have any problems, checkout the troubleshooting section at the bottom.

    Go to main directory of Animation Nodes. This folder should contain a file called ``setup.py``.

    Run ``python setup.py``. This can take a while.

    It also creates a ``config.py`` file next to the ``setup.py``. You can use it to specify where the compiled addon should be copied. This should be the path to Blenders addon directory. Once you changed the file, you can the ``setup.py`` file again. This time it copies all files into the specified location.

    Later when you want to recompile AN, just run ``python setup.py``. It will only recompile and copy the files that changed.


The ``setup.py`` file has a few command line arguments:

    - ``--all``
        This will rebuild all cython files which can be quite useful when
        Cython does not automatically detect all files that need to update
        after you've made a change. Should not be needed in most cases though.
    - ``--export``
        Create an ``animation_nodes.zip`` file that can be shared with others.
    - ``--nocopy``
        Don't copy the compiled build over to Blenders addon directory.


Troubleshooting
***************

If your problem cannot be solved with the information, please
`report <https://github.com/JacquesLucke/animation_nodes_manual/issues/new>`_ it.

Most errors happen because Python cannot find a correct C compiler to compile the extension modules. Here are some very helpful links on the topic:

- `Python Windows Compilers <https://wiki.python.org/moin/WindowsCompilers>`_
- `Compile C extensions on Windows 10 and Visual Studio 2017 <http://cs.mcgill.ca/~mxia3/2017/04/05/Compiling-Python-package-with-C-extension-on-Windows-10-and-Visual-Studio-2017/>`_

Basicly you will have to install Visual Studio 2017 (Microsoft does not want you to install older versions) and use the ``x64 Native Tools Command Prompt for VS 2017`` to run the ``python setup.py`` command.

Using Visual Studio 2015
------------------------

If Visual Studio 2015 is already installed on you machine but you get this error: ``unable to find vcvarsall.bat`` it is relatively easy to fix:

You need to change the installation installed features. More information can be found here: http://stackoverflow.com/a/35243904/4755171
