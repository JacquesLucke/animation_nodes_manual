---
title : Distribute Matrices
---

## Description

This node creates a list of matrices that represent the locations of object
distributed someway in space. They can be distributed in a line, grid, circle,
spiral, or based on a custom distribution.

## Linear

This option distribute matrices along an axis.

### Options

- **Direction Axis** - The axis at which the matrices are distributed.
- **Center** - If true, the matrices will be centered, otherwise, they will be
  distributed in the positive direction of the chosen axis.

### Size

This option lets you define the size of the line explicitly.

#### Inputs

- **Amount** - Number of matrices.
- **Size** - Size of the line.

### Step

This option lets you define the distance between each two consecutive matrices.
                
- **Amount** - Number of matrices.
- **Distance** - Distance between each two consecutive matrices.

## Grid

This option distribute matrices on a 3D lattice.

### Options

- **Center X** - Center grid along the X axis.
- **Center Y** - Center grid along the Y axis.
- **Center Z** - Center grid along the Z axis.

### Size

This option lets you define the dimensions of the lattice.

#### Inputs
                
- **X Division** - Number of matrices in x-axis.
- **Y Division** - Number of matrices in y-axis.
- **Z Division** - Number of matrices in z-axis.
- **Width** - The width of the lattice.
- **Length** - The length of the lattice.
- **Height** - The height of the lattice.
        
### Step

This option lets you define the distance between each two matrices in all axis.

#### Inputs
                
- **X Division** - Number of matrices in x-axis.
- **Y Division** - Number of matrices in y-axis.
- **Z Division** - Number of matrices in z-axis.
- **X Distance** - Distance between each two consecutive matrices along x-axis.
- **Y Distance** - Distance between each two consecutive matrices along y-axis.
- **Z Distance** - Distance between each two consecutive matrices along z-axis.

## Circle

This option lets you distribute matrices around a circle centered at the world.
        
### Inputs

- **Amount** - The number of matrices around the circle.
- **Radius** - Radius of the circle.
- **Segment** - A ratio that describe the completeness of the circle, where `1`
  means a complete circle and `0` means no circle.

## Mesh

This option lets you distribute matrices along the vertices or polygons of a
mesh. The orientation of the matrices align with the normals of the vertices
and polygons.
        
### Inputs

- **Mesh** - The input mesh.

## Spiral

This option lets you distribute matrices along a spiral.

### Options

- **Center Spiral** - If true, the spiral will be centered vertically.

### Inputs

- **Amount** - The amount of matrices to compute.
- **Start Radius** - The distance from the center where the spiral will start.
- **End Radius** - The distance from the center where the spiral will end.
- **Start Size** - The scale of the matrix at the start of the spiral.
- **End Size** - The scale of the matrix at the end of the spiral.
- **Start Angle** - The angle from the positive X axis where the spiral will
  start. Angles can't be equivalent.
- **End Angle** - The angle from the positive X axis where the spiral will end.
  Angles can't be equivalent.
- **Height** - The height of the spiral. A zero height means a spiral lying on
  the XY plane.
- **Radius Interpolation** - An interpolation controlling the rate of change of
  the radius. For instance, an ease-in interpolation would mean the spaces
  betweens the arms of the spiral closer to the center will be larger than the
  spaces between the arms of the spiral away from the center.
- **Height Interpolation** - An interpolation controlling the rate of change of
  the height. For instance, an ease-in interpolation would mean the vertical
  spaces betweens the arms of the spiral closer to the start will be larger than
  the vertical spaces between the arms of the spiral away from the start.

## Spline

This option lets you distribute matrices along a spline. The matrices are
oriented such that its local axis align with the tangent and normal to the
spline.

### Options

- **Uniform** - Distribute the matrices uniformly such that the matrices would
  have equal distances along the spline.
- **Step** - Distribute the matrices uniformly given the input step size.
- **Resolution** - Distribute the matrices based on the density of the spline.
- **Vertices** - Distribute the matrices along the vertices of the spline.

### Inputs

- **Spline** - The spline to evaluate.
- **Count** - The amount of matrices to compute. (Only available in the
  *Uniform* and *Resolution* options.)
- **Step** - The step size to use for the *Step* option.
- **Start** - The start parameter to start evaluating at.
- **End** - The end parameter to stop evaluating at.
- **Use Radius** - If true, the matrices will be scaled by the radius of the
  spline.

### Advanced Node Settings

- **Resolution** - It is the quality of the evaluated spline, in other words, it
  is the number of point in the spline used in evaluation.

## Outputs

- **Matrices** - The output matrices.
- **Vectors** - The locations of the output matrices.
