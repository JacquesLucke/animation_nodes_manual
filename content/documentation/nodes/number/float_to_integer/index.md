---
title : To Integer
weight : 1
---

## Description

This node converts floats into integers using one of 3 algorithms. (See
advanced node settings)

![image](to_integer_node.png)

## Inputs

  - **Float** - A float to convert to integer.

## Outputs

  - **Integer** - Output as integer.

## Advanced Node Settings

The node has 3 algorithms to do the conversion:

  - **Floor** - It returns only the whole number.
  - **Ceiling** - It returns the next whole number.
  - **Round** - Standard round operation, where *floor* is used if the
    fraction is less than or equal 0.5 and *ceiling* is used if the
    fraction is larger than 0.5.

<table style="width:51%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>Float</th>
<th>Floor</th>
<th>Ceiling</th>
<th>Round</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0.1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td>0.6</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>1.1</td>
<td>1</td>
<td>2</td>
<td>1</td>
</tr>
<tr class="even">
<td>1.6</td>
<td>1</td>
<td>2</td>
<td>2</td>
</tr>
<tr class="odd">
<td>2.1</td>
<td>2</td>
<td>3</td>
<td>2</td>
</tr>
</tbody>
</table>
