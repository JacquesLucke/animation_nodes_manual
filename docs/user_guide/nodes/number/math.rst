Math
====

Description
-----------
This node carry 26 math operation:

- **Add** - Adds input A to input B.

- **Subtract** - Subtract input B from input A.

- **Multiply** - Multiply input A by input B.

- **Divide** - Divides input A by input B.

- **Sine** - Calculate the sin of input A.

- **Cosine** - Claculate the cosine of input A.

- **Tangent** - Calculate the tangent of input A.

- **Arcsine** - Calaculate the arcsine of input A.

- **Arccosine** - Calculate the arccosine of input A.

- **Arctangent** - Calculate the arctangent of input A.

- **Power** - Returns input A to the power of input B.

- **Logarithm** - Returns the logarithm of input A to the base input B.

- **Minimum** - Returns the smallest value from input A and input B.

- **Maximum** - Returns the largest value from input A and input B.

- **Modulo** - Returns the remainder of divinding input A by input B.

- **Absolute** - Returns the positive value of input A.

- **Floor** - Returns the whole number of input A.

- **Ceiling** - Returns the next whole number after input A.

- **Square Root** - Returns the square root of input A.

- **Invert** - Flips the sign of input A.

- **Reciprocal** - Returns the mathematical inverse of input A (1/A).

- **Snap** - Snaps input A to the whole multiples of the Step Size.

- **Arctangent B/A** - Returns the arctangent of input B divided by input A.

- **Hypotenuse** - Returns the length of the hypotenuse given the side length input A and B.

- **Copy Sign** - Returns input A with the sign of input B.

- **Floor Division** - Returns the whole number of input A divided by input B.


.. image:: images/math_node.png

Inputs
------

- **A** - Input A.
- **B** - Input B.

(Inputs are dynamic, Means the node has either one or two inputs based on selected operation.)

Outputs
-------

- **Result** - The result of the math operation.

Advanced Node Settings
----------------------

N/A

Notes
-----

- Division by 0 returns 0.0.
- Logarithm with the base <=0 or =1 takes the natural logarithm.
- Modulo by 0 returns 0.0.
