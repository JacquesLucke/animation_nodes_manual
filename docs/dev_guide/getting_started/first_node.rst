*******************
Creating a new Node
*******************

A node is a single python file. All registration is done automatically.


1.  a) Choose one of the existing node categories (folders inside the ``nodes\\`` directory) or
    b) Create a new category. To do that make a new folder and put an empty file called ``__init__.py`` inside.


2.  Create a new python file inside the category you choosed: ``nodes\\$category$\\$node_name$.py``


3.  Copy the template in:

    .. code-block:: python
        :linenos:

        import bpy
        from ... base_types.node import AnimationNode

        class TEMPLATENode(bpy.types.Node, AnimationNode):
            bl_idname = "an_TEMPLATENode"
            bl_label = "TEMPLATE"

            def create(self):
                pass

            def execute(self):
                return
