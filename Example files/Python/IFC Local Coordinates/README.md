# How-To
- Download or Copy the script in a main.py.
- Create an 'output' folder and a 'model' folder.
- Add the models for test in the model folder.
- Change the main.py to Load the correct model, before running the code.


# IFC Local Coordinates Script

This Scripts is created to get local placement of all elements in excel.
Its based of https://github.com/IfcOpenShell/IfcOpenShell/issues/688 
Shoutout to aothm for the base of the code and Moult for debugging it.

Also take a look at this link to understand placement in IFC better: https://pythoncvc.net/?p=851


# Output Information

x, y and z is direction Vectors.
t is the translation
The last vector [0,0,0,1] is w
This defines if the matrix is a diretion or a position in space.

[ x0  y0  z0  t0 ]
[ x1  y1  z1  t1 ]
[ x2  y2  z2  t2 ]
[  0   0   0   1 ]


# Using placement matrix

As stated in its source code when you create a geom. Its location is given by a 4×3 matrix. 
But care, when displayed as a tuple IfcOpenShell matrix and FreeCAD matrix are transposed :

    IfcOpenShell matrix values is a tuple of 4 consecutive vector’s xyz :
    format : (v1.x, v1.y, v1.z, v2.x, v2.y … , v4.z)
    FreeCAD matrix constructor takes up to 16 float. 4 vectors grouped by x, y, z values :
    format : (v1.x, v2.x, v3.x, v4.x, v1.y, … , v4.z, 0, 0, 0, 1)

About the last 0, 0, 0, 1 of FreeCAD matrix. As greatly stated in matrices chapter from the OpenGL tutorial :

    This will be more clear soon, but for now, just remember this :
    If w == 1, then the vector (x,y,z,1) is a position in space.
    If w == 0, then the vector (x,y,z,0) is a direction.
    (In fact, remember this forever.)
    http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/
