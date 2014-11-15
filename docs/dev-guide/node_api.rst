********
Node API
********

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


There are 2 different main methods how a node can be executed:

Execute Function
################

The node has a function called ``execute``, which has the socket values as input and the corresponding output.
The easiest way to use this is the Dictionary-Mode.

Dictionary-Mode:
****************

This means that you have only one input variable next to ``self`` which is a Dictionary. The keys are the socket identifiers (name). The function must return another dictionary.

.. code-block:: python
    :linenos:
    
    def execute(self, input):
        output = {}
        
        if input["Condition"]:
            output["Text"] = "Yes"
        else: output["Text"] = "No"
        
        return output
        

With defined socket names: 
**************************

This is a slightly faster method because there is less overhead creating dictionaries. Here you first have to define how your variables are named in the execute function.

.. code-block:: python
    :linenos:
    
    # example from animate float node
    def getInputSocketNames(self):
		return {"Start" : "start",
                "End" : "end",
                "Time" : "time",
                "Interpolation" : "interpolation", 
                "Duration" : "duration", 
                "Delay" : "delay"}
	def getOutputSocketNames(self):
		return {"Current" : "current", 
                "New Time" : "newTime", 
                "Difference" : "difference"}
                
The execute function uses these names as parameters. Note that the return order has to be the same like the output socket order.

.. code-block:: python
    :linenos:
    
    def execute(self, useOutput, start, end, time, interpolation, duration, delay):
		duration = max(duration, 1)
		influence = interpolation[0](max(min(time / duration, 1.0), 0.0), interpolation[1])
		current = start * (1 - influence) + end * influence
		difference = 0
		if useOutput["Difference"]:
			influence = interpolation[0](max(min((time - 1)/ duration, 1.0), 0.0), interpolation[1])
			oldResult = start * (1 - influence) + end * influence
			difference = current - oldResult
		return current, time - duration - delay, difference
        
        
In-Line Execution
#################

TODO