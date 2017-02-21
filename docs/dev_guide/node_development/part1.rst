Node Development - Part 1
=========================

Welcome to this introduction into node development in Animation Nodes 2.0 or higher. In this guide you will learn how to get started with writing your own nodes (and I suggest you learn this before you try to modify existing nodes!). It will consist of multiple parts. Each part will go a bit more into detail so that you will be able to write more complex nodes in the end.

To develop your own nodes you have to setup your development environment first. There are basicly two possible setups:

1. Complete Setup:
    This mainly means that you are working in the real git repository of Animation Nodes. You will have to make sure that you can compile the code etc. More information on how to do that can be found here: :ref:`setup-environment`
2. Lightweight Setup:
    The easiest way to start developing your own stuff. Basicly you just install the addon normally and work directly in Blenders addon folder. I definitly suggest to use this method at first because you can forget about compiling and all that stuff that can cause trouble. So if you have AN already installed you don't need to do anything.


Once you setup everything, you'll have to choose where to put your new node in the existing code base. Usually all nodes are in a subdirectory of the ``animation_nodes/nodes/`` folder. However, they can be anywhere in the Animation Nodes package. You can even decide to to create your own folder for your nodes. In that case don't forget to also create a new empty ``__init__.py`` file in that new folder. It tells Python that this folder is part of Animation Nodes.

For this tutorial I suppose that the new file will be in a folder like ``animation_nodes/nodes/category/``. If you put it somewhere else you have to adjust the relative imports accordingly.

Now you are ready to create the actual file. Since Animation Nodes 2.0 there are two different types of source code files:

1. Python files: ``.py``
    These are just normal python files. If you choosed the lightweight setup you have to use this type. Most nodes should be of this type, there are only a very few nodes which aren't. I suggest to choose this type always at this stage. It will be easy to change it later if necessary.
2. `Cython`_ files: ``.pyx``
    Cython is another programming language that builds on top of Python. The main benefit is that it can be compiled into machine code which can make it much faster than normal python code. For most nodes this is absolute overkill, the performance benefit will only be visible be computational expensive operations. Also you can only work with Cython files when you setup the complete working environment.

.. _Cython: http://www.cython.org/
