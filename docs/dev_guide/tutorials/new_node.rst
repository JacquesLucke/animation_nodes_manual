Creating a new Node
*******************

Note: This step-by-step guide only works in after the v1.6 release.

1.  Create a **new file** for the new node. Normally this should be inside a
    *nodes/category/* folder but it can be anywhere. If you create a new category
    don't forget to also insert an empty ``__init__.py`` inside that folder.

2.  Insert the **template**. This is only one possible structure for nodes but
    it's the easiest to start with. Here is a small overview for what the two
    class properties are used:

        - ``bl_idname``
                This an identifier for the node, changing it
                breaks all files in which this socket is used.
        - ``bl_label``
                This label is used in the search, it is also the
                default name and label of the node.

    .. code-block:: python
        :linenos:

        import bpy
        from ... base_types.node import AnimationNode

        class TemplateNode(bpy.types.Node, AnimationNode):
            bl_idname = "an_TemplateNode"
            bl_label = "Template"

            def create(self):
                pass

            def execute(self):
                pass

3.  Replace ``Template`` with the name of your node.

When you restart Blender now you should already see this node in the Search (ctrl-A).
Obviously it does nothing yet, so let's go further.


Creating Sockets
****************

The ``create(self)`` method is called once when the node is created. So it can be
used to initialize the node. Sockets can be created using the ``newInput`` and
``newOutput`` function. They both take these arguments (in this exact order):

    - ``dataType``:
            This can be either the ``bl_idname`` or the ``dataType`` attribute
            of the socket you want to create. Writing ``an_VectorSocket`` or just
            ``Vector`` has the same effect but using the shorter version is prefered.
    - ``name``:
            The text that will be shown in the socket in the node editor.
            It doesn't have to be unique in the node but it should be.
    - ``identifier``:
            (optional but should be given in most cases) Unique name of the socket.
            Should be a valid Python identifier (no spaces, ...).
    - ``**kwargs``:
            (optional) Convenient way to set some default properties on
            the new socket.

.. code-block:: python
    :linenos:

    def create(self):
        # most common data types are:
        #   Integer, Float, Vector, String, Boolean, Object, ...
        # both functions return the newly created socket
        self.newInput("Integer", "Number", "number")
        self.newInput("Float", "Factor", "factor", value = 5.0)
        self.newInput("Object", "Target", "target")

        self.newOutput("String", "Text", "text")
        self.newOutput("Vector", "Result", "result")

Now the ``execute`` method has to change to make the node work again. Basicly
the execute method takes the value of the sockets in order and returns the values
for the output sockets in order. It's good practice to use the variable names
you specified as socket identifiers.

.. code-block:: python
    :linenos:

    def execute(self, number, factor, target):
        # do some work ...
        return text, result

It's very important that the returned variables always have the correct type.
eg the function should never return ``None`` when a vector is expected (an
object on the other hand can be ``None``).
