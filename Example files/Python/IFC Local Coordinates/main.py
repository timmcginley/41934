"""
This Scripts is created to get local placement of all elements in excel.
Its based of https://github.com/IfcOpenShell/IfcOpenShell/issues/688 
Shoutout to aothm for the base of the code and Moult for debugging it.

Also take a look at this link to understand placement in IFC better: https://pythoncvc.net/?p=851
"""

import os
import time
import ifcopenshell
import ifcopenshell.geom
from ifcopenshell import geom
import numpy as np
import xlsxwriter

settings = ifcopenshell.geom.settings()

#Load File and Time it
timeStart = time.perf_counter()

FindDIR = os.path.dirname(os.path.abspath(__file__))
InternalPATH = "model"

aNugget = os.path.join(FindDIR, InternalPATH, "BIM_Projekt_Golden_Nugget-Architecture_Structural_optimized.ifc")
mepNugget = os.path.join(FindDIR, InternalPATH, "BIM_Projekt_Golden_Nugget-Building_Services_optimized.ifc")
aDuplex = os.path.join(FindDIR, InternalPATH, "Duplex_A_20110907_optimized.ifc")
mepDuplex = os.path.join(FindDIR, InternalPATH, "Duplex_M_20111024_optimized.ifc")

"""
##########################################################################################
In the model variable you can change the variable to get location data of different models.
##########################################################################################
"""
model = ifcopenshell.open(aDuplex)
print("\nIt took {} second to load Model\n".format(time.perf_counter()-timeStart))

#Find XLSX Output Path
OutputPATH = os.path.join(FindDIR, "output\\future_format.xlsx")
workbook = xlsxwriter.Workbook(OutputPATH)

worksheet = workbook.add_worksheet("Summary")
text = "This workbook contain location information. For now the information is represented as coordinates relative to other objects in the ifc three up through IfcBuilding, IfcSite and IfcProject. For shape geometric data another software might be needed to be able to read the data, and analyze it. As for IfcOpenShell comments on Github advise against shape manipulation, as it would be too complex."

worksheet.write(0,0,text)

#Create a list with possible Entities
productList = []
for product in model.by_type("IfcProduct"):
    productList.append(product.is_a())
productList = list(set(productList))
productList.sort()

#Functions To define the matrix placement of an object.
def a2p(o,z,x):
    y = np.cross(z, x) 
    r = np.eye(4) 
    r[:-1,:-1] = x,y,z 
    r[-1,:-1] = o 
    return r.T
    
def axis2placement(plc): 
    z = np.array(plc.Axis.DirectionRatios if plc.Axis else (0,0,1)) 
    x = np.array(plc.RefDirection.DirectionRatios if plc.RefDirection else (1,0,0)) 
    o = plc.Location.Coordinates 
    return a2p(o,z,x) 
    
def local_placement(plc):
    if plc.PlacementRelTo is None: 
        parent = np.eye(4)
    else:
        parent = local_placement(plc.PlacementRelTo)
    # print(plc.RelativePlacement)
    return np.dot(parent, axis2placement(plc.RelativePlacement))

for product in productList:
    if product in productList:
        i=1
        worksheet = workbook.add_worksheet(product)
        worksheet.write(0,0,"Name")
        worksheet.write(0,1,"X")
        worksheet.write(0,2,"Y")
        worksheet.write(0,3,"Z")
        worksheet.write(0,4,"Position")
        worksheet.write(0,5,"Tag")
        print("Checking element {}".format(product))

        for entity in model.by_type(product):
            m = local_placement(entity.ObjectPlacement)
            entity_matrix = np.matrix([
                [m[0][0], m[1][0], m[2][0], 0],
                [m[0][1], m[1][1], m[2][1], 0],
                [m[0][2], m[1][2], m[2][2], 0],
                [m[0][3], m[1][3], m[2][3], 1]])
            entity_matrix.transpose()

            Vector_x = (m[0][0],m[1][0],m[2][0])
            Vector_y = [m[0][1],m[1][1],m[2][1]]
            Vector_z = [m[0][2],m[1][2],m[2][2]]
            Position = [m[0][3],m[1][3],m[2][3]]

            # print(Vector_x, Vector_y, Vector_z, Position)
            
            worksheet.write(i,0,str(entity.Name))
            worksheet.write(i,1,str(Vector_x))
            worksheet.write(i,2,str(Vector_y))
            worksheet.write(i,3,str(Vector_z))
            worksheet.write(i,4,str(Position))
            if entity_matrix[3,3] == 0:
                worksheet.write(i,5,"Direction")
            elif entity_matrix[3,3] == 1:
                worksheet.write(i,5,"Position in Space")

            i+=1

            # print(entity)
            # print(entity_matrix)
            # print(entity_matrix.transpose())

"""
x, y and z is direction Vectors.
t is the translation
The last vector [0,0,0,1] is w
This defines if the matrix is a diretion or a position in space.

[ x0  y0  z0  t0 ]
[ x1  y1  z1  t1 ]
[ x2  y2  z2  t2 ]
[  0   0   0   1 ]
"""


"""
Using placement matrix

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
"""

workbook.close()