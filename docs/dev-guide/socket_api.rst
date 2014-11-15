**********
Socket API
**********

Every socket is a subclass of ``mn_node_base.mn_BaseSocket`` and ``mn_node_base.mn_SocketProperties``. The ``bl_idname`` should be the same as the class name and the bl_label a more readable Version.

.. code-block:: python
    :linenos:
    
    class mn_VectorSocket(mn_BaseSocket, mn_SocketProperties):
        bl_idname = "mn_VectorSocket"
        bl_label = "Vector Socket"
        dataType = "Vector"
        allowedInputTypes = ["Vector"]
        drawColor = (0.05, 0.05, 0.8, 0.7)
   
   
**dataType:** The type that the socket outputs. Should be as short and understandable as possible.
**allowedInputTypes:** These types are like subtypes and are internally convertable into ``dataType``. Use ``"all"`` if the user can make a link from everywhere to here (used in ``Generic`` and ``Empty`` socket).
**drawColor:** RGBA tupel of the color being used to draw this socket in the node editor.

In addition to that the socket needs a ``drawInput`` function. This is called when an input socket is unconnected.

.. code-block:: python
    :linenos:
    
    # from Vector Socket
    def drawInput(self, layout, node, text):
		col = layout.column(align = True)
		col.label(text)
		col.prop(self, "vector", index = 0, text = "X")
		col.prop(self, "vector", index = 1, text = "Y")
		col.prop(self, "vector", index = 2, text = "Z")
		col.separator()
        
The ``getValue`` function must return an instance of the data type declared above.

.. code-block:: python
    :linenos:
    
    def getValue(self):
		return self.vector
        
The ``getStoreableValue`` and ``setStoreableValue`` functions are used by some internal code. The data they return has to be save to be stored even if an object in Blender is deleted or so.

.. code-block:: python
    :linenos:
    
    def setStoreableValue(self, data):
		self.vector = data
	def getStoreableValue(self):
		return self.vector[:]
