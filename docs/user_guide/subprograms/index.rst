Subprograms
===========

.. toctree::
   :titlesonly:

   Group <group>
   Loop <loop>
   Script <script>

Node trees you create can be considered as programs but in a visual form. Those node trees may contain portions where node setups are similar or with slightly different parameters, copying the same node setup to multiple locations in the node tree would be extremely inefficient. Likewise, one may need to apply the same node setup to multiple objects, doing that manually would also be inefficient and tedious.

Animation Nodes provide us with Subprograms which are smaller node trees that can be created once and used all over the node tree as much as needed.

Animation Nodes have three types of subprograms which can all be called using the **Invoke Subprogram** node after they are defined. Such subprograms should be independent of of the node tree itself, so you can't use a node that depend on the subprogram inside the subprogram. So it is recommended that you put all your subprograms in a portion of the node editor away from the node tree itself.
