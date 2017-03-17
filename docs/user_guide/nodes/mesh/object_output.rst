Object Output
=============

Description
-----------
This node edits the input object's data based on a new input data.

.. image:: images/mesh_object_output_node.png
   :width: 200pt

Options
-------
- **Mesh Data** - This option lets you write a mesh data block to the input object. Since the mesh data block carries only the vertices locations, edge, indices, and polygons indices info, those will be the only data in the output object. (A bmesh data block carries more information than the mesh data block like vertices normals.)
- **Bmesh** - This option lets you write a bmesh data block to the input object. A bmesh data block carry much more information than the mesh data block, such extra informations like *Vertex Normals*, *Vertex group weights* and *Material indices*.
- **Vertices** - This option will only edit the vertices locations, that is, the input object should already have some data and you are just editing the vertices locations of this data. This option is much faster than the **Mesh Data** option assuming all you do is edit the vertices.

Inputs
------

- **Object** - An object to edit, The plus button let you add a new object and write to it.
- **Mesh Data** - Mesh data to write to the input object. (Only for the Mesh Data option)
- **Bmesh** - Bmesh to write to the input object. (Only for the Bmesh option)
- **Vertices** - Vector list that represents the new locations for the vertices. (Only for the vertices option)
- **Material Indices** - An integer list, the 1st integer represent the index of the material of the 1st polygon, the 2nd integer represent the index of the material of the 2nd polygon, ....


Outputs
-------

- **Object** - The input object.

Advanced Node Settings
----------------------

- **Check Indices** - If enabled, AN will compare the indices of polygons and edges to the vertex data checking to see if they are consistent, if they are not, the node will return an error and stop excuting. (The node will execute faster if this option is disabled **But** don't do that unless you are sure that your data is valid because if it is not, blender may crash.)
- **Check Tuple Lengths** - If enabled, AN will check the number of elements in each polygon and edge indices, if the number of elements in the edge indices is not 2 or the number of elements in polygon indices is less than 3, the node will return an error and stop excuting.

Examples of Usage
-----------------

.. image:: gifs/object_mesh_data_node_example.gif
