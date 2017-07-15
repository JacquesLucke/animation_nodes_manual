Object Output
=============

Description
-----------

This node edits the input object's data based on a new input data.

.. image:: images/mesh_object_output_node.png
   :width: 200pt

Options
-------

- **Mesh Data** - This option lets you write a mesh data to the input object. Since the mesh data block carries only the vertices locations, edge, indices, and polygons indices info, those will be the only data in the output object. (A bmesh data carries more information than the mesh data block like vertices normals.)
- **Bmesh** - This option lets you write a bmesh data to the input object. A bmesh data carry much more information than the mesh data, such extra information like *Vertex Normals*, *Vertex group weights* and *Material indices*.
- **Vertices** - This option will only edit the vertices locations, that is, the input object should already have some data and you are just editing the vertices locations of this data. This option is much faster than the **Mesh Data** option assuming all you do is edit the vertices.

Inputs
------

- **Object** - An object to edit. The plus button let you add a new object and write to it.
- **Mesh Data** - Mesh data to write to the input object. (Only for the Mesh Data option)
- **Bmesh** - Bmesh to write to the input object. (Only for the Bmesh option)
- **Vertices** - Vector list that represents the new locations for the vertices. (Only for the vertices option)
- **Material Indices** - An integer list, the first integer represent the index of the material of the first polygon, the 2nd integer represent the index of the material of the 2nd polygon, ....


Outputs
-------

- **Object** - The input object.

Advanced Node Settings
----------------------

- **Make Mesh Exportable** - If enabled, the mesh will be edited in order to be exported correctly. Use when exporting using Alembic.
- **Validate Mesh** - If enabled, animation nodes will check if the mesh data is valid and if not, it will try to correct it as much as possible. This option should always be enabled to avoid blender crashes. However, if you are absolutely sure that your mesh data is valid, you should disable it because it slows down execution. 
- **Print Validation Info** - If enabled and **Validate Mesh** is enabled, animation nodes will print the procedures taken to fix the input mesh data.

Examples of Usage
-----------------

.. image:: gifs/object_mesh_data_node_example.gif
