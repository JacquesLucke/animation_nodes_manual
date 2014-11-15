Node API
========

Every Node is a subclass of ``bpy.types.Node`` and ``mn_node_base.AnimationNode``. A node has at least two properties: ``bl_idname`` and ``bl_label``. The id-name should be the class name.

Furthermore every node has an ``init`` function that looks like this:

.. code-block:: python
    :linenos:
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_VectorSocket", "Position")
		self.inputs.new("mn_VectorSocket", "Rotation")
		self.inputs.new("mn_VectorSocket", "Scale").vector = [1, 1, 1]
		self.outputs.new("mn_MatrixSocket", "Matrix")
		allowCompiling()
		
This is mostly used to create sockets that a node has after creation.
``forbidCompiling()`` and ``allowCompiling`` should always be used to avoid some errors, because so the addon executes the node not until every socket is created.


There are several execution models a node can follow.

Dictionary Mode
^^^^^^^^^^^^^^^