# IfcOpenShell Examples

* N.B. in these examples for consistency we name the model 'model'; if you are using somethign different that is ok, but the idea here is to keep the code consistent to help you.

## Loading and importing the model and ifcOpenShell into the [IDE] you are using

If in Blender do....

```python

import bpy
from blenderbim.bim.ifc import IfcStore
model = IfcStore.get_file()

```

If in the console / terminal do...

```python
import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')
```

## Summary

#### Basic Scripts

* [Basic 1A - Space count check](#Basic-Example-1a)
* [Basic 1B - Space count check - with len()](#Basic-Example-1b)
* [Basic 2 - Total beam length in model)](#Basic-Example-2)
* [Basic 3 - Get element PropertySets](#Basic-Example-3)
* [Basic 4 - Door code check](#Basic-Example-4)
* [Basic 5 - model load time](#Basic-Example-5)
* [Basic 6 - Get beam properties](#Basic-Example-6)

#### Intermediate Scripts

* [Intermediate 1 - Get doors that bound a space (BoundedBy)](#Intermediate-Example-1) - check!
* [Intermediate 2 - Get doors that bound a space (BoundedBy)](#Intermediate-Example-2) - is repeat?
* [Intermediate 3 - Open a file with a window using TKinter](#Intermediate-Example-3)
* [Intermediate 4A - Write data to excel files](#Intermediate-Example-4a)
* [Intermediate 4B - Write ifc data to excel files](#Intermediate-Example-4b)
* [Intermediate 4C - Write ifc data to excel files (in a function)](#Intermediate-Example-4c)
* [Intermediate 5A - read data from excel files](#Intermediate-Example-5a)
* [Intermediate 5B - read data from excel file and IFC file](#Intermediate-Example-5b)
* [Intermediate 6 - tKinter GUI](#Intermediate-Example-6)

#### Advanced
* [Advanced 1 - element count by property and entity as function](#Advanced-Example-1)
* [Advanded 2 - define a simple wall](#Advanced-Example-2)
* [Advanced 4 - Define class and function to load models](#Advanced-Example-4)
* [Advanced 5A - Compare Geomtery in different models](#Advanced-Example-5a)
* [Advanced 5B - Collision functions](#Advanced-Example-5b)
* [Advanced 6 - (FAST) Property queries using selector](#Advanced-Example-6)
* [Advanced 7A - Check number of stories in different models](#Advanced-Example-7a)
* [Advanced 7B - Compare storey ELEVATIONS in different models](#Advanced-Example-7b)
* [Advanced 7C - Are the ELEVATIONS the same?](#Advanced-Example-7c)
* [Advanced 8A - Property check](#Advanced-Example-8a) - check!
* [Advanced 8B - Generic Property list](#Advanced-Example-8b)
* [Advanced 8C - Find entities from singlevalue property](#Advanced-Example-8c)
* [Advanced 9a - Door code check](#Advanced-Example-9a)

Rule: Check the number of spaces in the model

## Basic Examples

### Basic Example 1a
loop through the [entities] and then add one to the variable *spaces_in_model* each time we find an instance of that entity.

*remember to import ifcopenshell and load the model if you need to, see the [introduction](#Introduction) of this concept for more information.*

```python

spaces_required = 21
spaces_in_model = 0

for entity in model.by_type("IfcSpace"):
    spaces_in_model+=1

print("\nThere are "+str(spaces_in_model)+" spaces in the model")

if (spaces_required == spaces_in_model):
    print ('RESULT: The number of spaces is correct')
else:
    print ('RESULT: The number of spaces is wrong')
```

### Basic Example 1b
Use len() to count the number of [entities] (without having to loop through all of them).

*remember to import ifcopenshell and load the model if you need to, see the [introduction](#Introduction) of this concept for more information.*

```python

spaces_required = 21
spaces_in_model = len(model.by_type("IfcSpace"))

print("\nThere are "+str(spaces_in_model)+" spaces in the model")

if (spaces_required == spaces_in_model):
    print ('RESULT: The number of spaces is correct')
else:
    print ('RESULT: The number of doors is wrong')
```

Rule: In this example we will try to quantify the length of the beam. We will base this on the for loop we defined in example 1A.

### Basic Example 2
Quantify [use] case code example

*remember to import ifcopenshell and load the model if you need to, see the [introduction](#Introduction) of this concept for more information.*

```python

total_beam_Length = 0

for entity in model.by_type("IfcBeam"):
    #we need to get the attributes
   for relDefinesByProperties in entity.IsDefinedBy:
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
            #and then get the attribute we are looking for
            if prop.Name == 'Length':
                #add the length to the total length
                total_beam_length += prop.NominalValue.wrappedValue

print("\nThere are "+str(total_beam_length)+" meters of beam in the model")

```

### Basic Example 3
Get the property sets of an element.

*remember to import ifcopenshell and load the model if you need to, see the [introduction](#Introduction) of this concept for more information.*

```Python

# this just gets you the entity, defined here as wall
# feel free to change this to your needs
# appending [0] to the end means that we only get the first entity
# if you remove the [0] you will get all the ifcwall entitities in the model.
# remember that IfcWall is only one of the ways that ifc describes walls (HINT: IfcWallStandardCase)

wall = model.by_type('IfcWall')[0]
for definition in wall.IsDefinedBy:
	# To support IFC2X3, we need to filter our results.
	if definition.is_a('IfcRelDefinesByProperties'):
		property_set = definition.RelatingPropertyDefinition
		# Might return Pset_WallCommon
		print(property_set.Name)

```

### Basic Example 4
Door code check.

```Python
 
###Doors### 
 
doors_required = 14 ### <- Expected value of doors ### 
doors_in_model = len(model.by_type("IfcDoor")) 
min_width_door = 0.77 
valid_doors=0 
invalid_doors=0 
 
print ('\n') 
 
# initial check to establish if we have the 'correct' number of doors 
if doors_required == doors_in_model: 
    print("Result matches expected value ({})".format(doors_required)) 
elif doors_required > doors_in_model: 
    print("There are more doors than expected") 
elif doors_required < doors_in_model: 
    print("There are less doors than expected")      
print ('\n')  
# check each door to see if it complies and count the valid ones 
for door in model.by_type("IfcDoor"): 
    print ("door with width: "+str(door.OverallWidth))   
    if door.OverallWidth>=min_width_door: 
        valid_doors+=1       
# now we have finished the counting we can pull back the indents and print the result         
print("\nThe width of {} doors is according to the Danish Regulations".format(valid_doors)) 
print("The width of {} doors is not according to the Danish Regulations".format(doors_in_model-valid_doors)) 
```
![image](https://github.com/timmcginley/41934/assets/1415855/88274058-a001-455a-8b6b-b123fb7feb54)

### Basic Example 5
This code gets the time taken to load a model.

*This code includes the import and model loading as it is a special case.*

```Python
import ifcopenshell
import time
import pandas

# starting time
start = time.time()

#model = ifcopenshell.open("model/BIM_3W_Team05_Sub01.ifc")
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")
end = time.time()

print()# total time taken
print(f"model load time is... {end - start}\n")

```

### Basic Example 6

*This code includes the import and model loading as it is a special case.*

```Python

## Run script in blender
import bpy
from blenderbim.bim.ifc import IfcStore

file = IfcStore.get_file()

### GET PROPERTIES ###

## Get attributes directly from the element
spaces = file.by_type("IfcSpace")

for space in spaces:
    print(space.LongName)

## go through all the beams in the model
beams = file.by_type("IfcBeam")

for beam in beams:
    beam.Name
    ## get property sets attached to beams through IsDefinedBy"
    for definition in beam.IsDefinedBy:
        
        ## To support IFC2X3, we need to filter our results.
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            
            
            ## Sort by the name of the propertySet
            if property_set.Name == "Pset_BeamCommon":
               for property in property_set.HasProperties:
                    
                    #print(property)
                    ## sort b the name of the property
                    if property.Name == "IsExternal":
                        print(property.NominalValue.wrappedValue)

### GET MATERIALS ###

## Through HasAssociations get the associated materials of the element
for beam in beams:
    for relAssociatesMaterial in beam.HasAssociations:
        print(relAssociatesMaterial.RelatingMaterial.Name)


### GET RELATING STRUCTURE ###

## Through ContainedInStructure get the inverse relation to the 
for beam in beams:
    for relContainedInSpatialStructure in beam.ContainedInStructure:
        print(relContainedInSpatialStructure.RelatingStructure.Name)

```

## Intermediate Python Scripts

### Intermediate Example 1 
Get the doors that bound a space (BoundedBy) 

This example works to get you the doors (line 13) that bound the space (line 8).

*remember to import ifcopenshell and load the model if you need to, see the [introduction](#Introduction) of this concept for more information.*

```Python

for space in model.by_type("IfcSpace"):
    near = space.BoundedBy
    print("\n\t####{}\n".format(space.Name))
    for objects in near:
        if (objects.RelatedBuildingElement != None):
            if (objects.RelatedBuildingElement.is_a('IfcDoor')):
                print(objects.RelatedBuildingElement.Name)

```
### Intermediate Example 2
Get the doors that bound a space (BoundedBy)

For this example we have to include an additional library, but it provides a really cool approach. Also please note that this example uses the optimized version of the Duplex model. This is also available in your models folder. Optimised versions of files are much smaller, they are optimized using a great tool (Solibri IFC Optimizer) from Solibri. The idea is that it can be used to make IFC files easier to share.

*This code includes the import and model loading as it is a special case.*

```Python

import ifcopenshell
# That was normal the new bit is this geom lib below
import ifcopenshell.geom
# ok, so we are calling it fn (for file name here) - lets stick to that
fn = "model/Duplex_A_20110907_optimized.ifc"


# based on the fn we can now create the model which is called f
f = ifcopenshell.open(fn)

# a specific wall is defined here based on its GlobalID
# we are working with standard files so you should also be able to find this.
# the small diff is that this is working on the optimized version
wall = f["2O2Fr$t4X7Zf8NOew3FLPP"]

# This is the magic code that loads the geometry for the models into its own model - so that we can query the geometry (and in this case the 
tree_settings = ifcopenshell.geom.settings()
tree_settings.set(tree_settings.DISABLE_OPENING_SUBTRACTIONS, True)
t = ifcopenshell.geom.tree(f, tree_settings)

# you need the code below in both RWTH and if running it directly.
for space in model.by_type("IfcSpace"):
    near = space.BoundedBy
    print("\n\t####{}\n".format(space.Name))
    for objects in near:
        if (objects.RelatedBuildingElement != None):
            if (objects.RelatedBuildingElement.is_a('IfcDoor')):
                print(objects.RelatedBuildingElement.Name)
```

### Intermediate Example 3
Load file using tKinter

*This code is only a snippet*

```Python

# thanks to https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog

from Tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

```

### Intermediate Example 4a

Write data to excel.

1) type in the cmd line

<pre>pip install xlsxwriter</pre>

2) in your python file  type

```

import xlsxwriter # https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1

workbook = xlsxwriter.Workbook('output/future_format.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write(0,0, 'hello world')

workbook.close()
```

### Intermediate Example 4b

Write ifc data to excel files.

*This code include the import and model loading as it is a special case.*

```Python

# https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1

import ifcopenshell
import xlsxwriter 

# this line opens the workbook, if it doesn't exist it makes it, otherwise
# it will overwrite the existing file.
# if it dpes already exist please close it otherwise it will not work (it cannot read open files)
workbook = xlsxwriter.Workbook('output/future_format.xlsx')
# you have the workbook open, now specify the sheet you want to write to
worksheet = workbook.add_worksheet()
# this is extra code that you can include to format the cells in your document. You could shange this to other examples. to create other effects.
bold = workbook.add_format({'bold': True})

# this line loads the ifc model into python. - careful most internet examples use ifc_model, 
# but we are using model here, so that it also works in RWTH viewer.
# When RWTH viewer loads the model in the GUI it calls it model.
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")

# this is normally formatted
worksheet.write(0,0, 'hello')

# in this line we have added the bold argument defined previously with the add_format command to define the format of the cell.
worksheet.write(0,0, 'hello', bold)

# when you have finished editing the document it is essential to close the workbook.
# these saves the document.
workbook.close()

```

### Intermediate Example 4c

Write ifc data to excel files (in a function)

*This code include the import and model loading as it is a special case.*

```Python
import ifcopenshell
# we will use the xlswriter library below to work with excel in python.
import xlsxwriter # https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1
# make a folder called output and then this line will make an 
# excel in there if one doesn't exist already
# N.B. remember to close the workbook if you have it open 
# BEFORE you run this script!
workbook = xlsxwriter.Workbook('output/test.xlsx')
# open the model as normally
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")
# this is a function it enables you to repeat the same command
# and reduce the amount of code that you have :)
# the function is called makeASheet - you can call it anything...
# it has a brackets after it, this is where the argument goes...
def makeASheet(ifcType):
    sheet = workbook.add_worksheet(ifcType)
    # define which row you want to start writing at.
    row =1
    for entity in model.by_type(ifcType):
        # this writes the data to the sheet
        # sheet.write(row, column, data)
        sheet.write(row,0,str(entity.Name))
        # this 'iterates' row so that each time we step down a row.
        # otherwise each new entry would overwrite the previous entry.
        row+=1
# here we can call the function and put it the argument
# in this case we are asking for the results of 
# different IFC entities to be written to their own sheets       
makeASheet('IfcSlab')
makeASheet('IfcWall')
makeASheet('IfcCovering')
makeASheet('IfcBeam')
# it is important to close the workbook afterwards
workbook.close()

```

### Intermediate Example 5a

Read data from excel files

*This code include the import and model loading as it is a special case.*

```Python
import xlrd
import ifcopenshell


## open the workbook
workbook = xlrd.open_workbook('output/future_format.xlsx')
## print the number of sheets in the workbook
print (workbook.nsheets)
## print the name of the sheets in the workbook
print (workbook.sheet_names())
## open the sheets by index - open the first sheet of the workbook
first_sheet = workbook.sheet_by_index(0)
## print the values in the first row of the first sheet
print (first_sheet.row_values(0))
## print the values in the first row of the first sheet
print (first_sheet.col_values(0))
## read the first cell in the first sheet
cell = first_sheet.cell(0,0)
## print the first cell
print (cell)
## print the value contained in the first cell
print (cell.value)

```

### Intermediate Example 5b

Read data from excel file and IFC file

*This code include the import and model loading as it is a special case.*

```Python

import xlrd
import ifcopenshell

'''
For this example we take values from our assumptions sheet
based on the the global ids of the slabs in the model
'''

model = ifcopenshell.open("model/Duplex_A_20110907.ifc")

## Open the workbook
workbook = xlrd.open_workbook('output/future_format.xlsx')

## Open the assumptions sheet in the workbook
assumptions_sheet = workbook.sheet_by_index(4)

## loops though the stairs in the model
for slab in model.by_type('IfcSlab'):
    ## get the global id of the stair
    id = slab.GlobalId
    ## loops through the values in the first column of assumptionStair sheet
    for i in range(0, len(assumptions_sheet.col_values(0))):
        ##Get the cells in column A
        cell = assumptions_sheet.cell(i,0)
        ##Get the value of the cells
        value = cell.value
        ## Check if the value in the cell is the same as the global id of the slab
        if id == value:
            ## if the same id - print the value of the column B
            print(assumptions_sheet.cell(i,1).value)

```

### Intermediate Example 6

tKinter GUI

*This code is only a snippet*

```Python

# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()

```

## Advanced Python Scripts

### Advanced Example 1

Element count by property and entity as function

*This code include the import and model loading as it is a special case.*

```Python

import ifcopenshell
import time
import bpy
import os

# starting time
start = time.time()

#model = ifcopenshell.open("model/BIM_3W_Team05_Sub01.ifc")
modelname = "Duplex_A_20110907.ifc"
modelpath = os.path.join(os.path.dirname(bpy.data.filepath), modelname)
model = ifcopenshell.open(modelpath)

end = time.time()

# total time taken
print(f"model load time is... {end - start}\n")

building = model.by_type('IfcBuilding')


def elCount(entityName,ifcClass):
    print("{} = {}".format(entityName,len(model.by_type(ifcClass))))
    
elCount("floors",'IfcBuildingStorey')   
elCount("beams",'IfcBeam')   
elCount("specialWalls",'IfcWall')
slabVol = 0
slab =model.by_type('IfcSlab')[0]
print(slab.IsDefinedBy)

elCount("standardWalls",'IfcWallStandardCase')
elCount("windows",'IfcWindow')  
elCount("doors",'IfcDoor')     
elCount("slabs",'IfcSlab')      

elevation = -20000
f2f = 0
floors = model.by_type('IfcBuildingStorey')

for floor in floors[::-1]:
    print ("\n_____ {} - {}".format(floor.Name,floor.Elevation))
    # get the f2f for the storey
    for relDefinesByProperties in floor.IsDefinedBy:
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
            #and then get the attribute we are looking for
            if prop.Name == 'height':
                #add the length to the total length
                print("found it!")
                f2f = prop.NominalValue.wrappedValue
            else:
                print("didn't find it! "+prop.Name+" : "+str(prop.NominalValue.wrappedValue))
    print(str(f2f)+"KDFKDFKMFGF----HK")
    for space in floor.IsDecomposedBy:

        for inst in space.RelatedObjects:
            print(inst)
```

### Advanded 2

define a simple wall

*This code include the import and model loading as it is a special case.*

```Python

import uuid
import time
import tempfile
import ifcopenshell

O = 0., 0., 0.
X = 1., 0., 0.
Y = 0., 1., 0.
Z = 0., 0., 1.

# Helper function definitions

# Creates an IfcAxis2Placement3D from Location, Axis and RefDirection specified as Python tuples
def create_ifcaxis2placement(ifcfile, point=O, dir1=Z, dir2=X):
    point = ifcfile.createIfcCartesianPoint(point)
    dir1 = ifcfile.createIfcDirection(dir1)
    dir2 = ifcfile.createIfcDirection(dir2)
    axis2placement = ifcfile.createIfcAxis2Placement3D(point, dir1, dir2)
    return axis2placement

# Creates an IfcLocalPlacement from Location, Axis and RefDirection, specified as Python tuples, and relative placement
def create_ifclocalplacement(ifcfile, point=O, dir1=Z, dir2=X, relative_to=None):
    axis2placement = create_ifcaxis2placement(ifcfile,point,dir1,dir2)
    ifclocalplacement2 = ifcfile.createIfcLocalPlacement(relative_to,axis2placement)
    return ifclocalplacement2

# Creates an IfcPolyLine from a list of points, specified as Python tuples
def create_ifcpolyline(ifcfile, point_list):
    ifcpts = []
    for point in point_list:
        point = ifcfile.createIfcCartesianPoint(point)
        ifcpts.append(point)
    polyline = ifcfile.createIfcPolyLine(ifcpts)
    return polyline
    
# Creates an IfcExtrudedAreaSolid from a list of points, specified as Python tuples
def create_ifcextrudedareasolid(ifcfile, point_list, ifcaxis2placement, extrude_dir, extrusion):
    polyline = create_ifcpolyline(ifcfile, point_list)
    ifcclosedprofile = ifcfile.createIfcArbitraryClosedProfileDef("AREA", None, polyline)
    ifcdir = ifcfile.createIfcDirection(extrude_dir)
    ifcextrudedareasolid = ifcfile.createIfcExtrudedAreaSolid(ifcclosedprofile, ifcaxis2placement, ifcdir, extrusion)
    return ifcextrudedareasolid
    
create_guid = lambda: ifcopenshell.guid.compress(uuid.uuid1().hex)

# IFC template creation

filename = "hello_wall.ifc"
timestamp = time.time()
timestring = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(timestamp))
creator = "Kianwee Chen"
organization = "ETHZ"
application, application_version = "IfcOpenShell", "0.5"
project_globalid, project_name = create_guid(), "Hello Wall"
    
# A template IFC file to quickly populate entity instances for an IfcProject with its dependencies
template = """ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');
FILE_NAME('%(filename)s','%(timestring)s',('%(creator)s'),('%(organization)s'),'%(application)s','%(application)s','');
FILE_SCHEMA(('IFC2X3'));
ENDSEC;
DATA;
#1=IFCPERSON($,$,'%(creator)s',$,$,$,$,$);
#2=IFCORGANIZATION($,'%(organization)s',$,$,$);
#3=IFCPERSONANDORGANIZATION(#1,#2,$);
#4=IFCAPPLICATION(#2,'%(application_version)s','%(application)s','');
#5=IFCOWNERHISTORY(#3,#4,$,.ADDED.,$,#3,#4,%(timestamp)s);
#6=IFCDIRECTION((1.,0.,0.));
#7=IFCDIRECTION((0.,0.,1.));
#8=IFCCARTESIANPOINT((0.,0.,0.));
#9=IFCAXIS2PLACEMENT3D(#8,#7,#6);
#10=IFCDIRECTION((0.,1.,0.));
#11=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.E-05,#9,#10);
#12=IFCDIMENSIONALEXPONENTS(0,0,0,0,0,0,0);
#13=IFCSIUNIT(*,.LENGTHUNIT.,$,.METRE.);
#14=IFCSIUNIT(*,.AREAUNIT.,$,.SQUARE_METRE.);
#15=IFCSIUNIT(*,.VOLUMEUNIT.,$,.CUBIC_METRE.);
#16=IFCSIUNIT(*,.PLANEANGLEUNIT.,$,.RADIAN.);
#17=IFCMEASUREWITHUNIT(IFCPLANEANGLEMEASURE(0.017453292519943295),#16);
#18=IFCCONVERSIONBASEDUNIT(#12,.PLANEANGLEUNIT.,'DEGREE',#17);
#19=IFCUNITASSIGNMENT((#13,#14,#15,#18));
#20=IFCPROJECT('%(project_globalid)s',#5,'%(project_name)s',$,$,$,$,(#11),#19);
ENDSEC;
END-ISO-10303-21;
""" % locals()

# Write the template to a temporary file 
temp_handle, temp_filename = tempfile.mkstemp(suffix=".ifc")
with open(temp_filename, "w") as f:
    f.write(template)

 
# Obtain references to instances defined in template
ifcfile = ifcopenshell.open(temp_filename)
owner_history = ifcfile.by_type("IfcOwnerHistory")[0]
project = ifcfile.by_type("IfcProject")[0]
context = ifcfile.by_type("IfcGeometricRepresentationContext")[0]

# IFC hierarchy creation
site_placement = create_ifclocalplacement(ifcfile)
site = ifcfile.createIfcSite(create_guid(), owner_history, "Site", None, None, site_placement, None, None, "ELEMENT", None, None, None, None, None)

building_placement = create_ifclocalplacement(ifcfile, relative_to=site_placement)
building = ifcfile.createIfcBuilding(create_guid(), owner_history, 'Building', None, None, building_placement, None, None, "ELEMENT", None, None, None)

storey_placement = create_ifclocalplacement(ifcfile, relative_to=building_placement)
elevation = 0.0
building_storey = ifcfile.createIfcBuildingStorey(create_guid(), owner_history, 'Storey', None, None, storey_placement, None, None, "ELEMENT", elevation)

container_storey = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Building Container", None, building, [building_storey])
container_site = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Site Container", None, site, [building])
container_project = ifcfile.createIfcRelAggregates(create_guid(), owner_history, "Project Container", None, project, [site])

# Wall creation: Define the wall shape as a polyline axis and an extruded area solid
wall_placement = create_ifclocalplacement(ifcfile, relative_to=storey_placement)
polyline = create_ifcpolyline(ifcfile, [(0.0, 0.0, 0.0), (5.0, 0.0, 0.0)])
axis_representation = ifcfile.createIfcShapeRepresentation(context, "Axis", "Curve2D", [polyline])

extrusion_placement = create_ifcaxis2placement(ifcfile, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
point_list_extrusion_area = [(0.0, -0.1, 0.0), (5.0, -0.1, 0.0), (5.0, 0.1, 0.0), (0.0, 0.1, 0.0), (0.0, -0.1, 0.0)]
solid = create_ifcextrudedareasolid(ifcfile, point_list_extrusion_area, extrusion_placement, (0.0, 0.0, 1.0), 3.0)
body_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [solid])

product_shape = ifcfile.createIfcProductDefinitionShape(None, None, [axis_representation, body_representation])

wall = ifcfile.createIfcWallStandardCase(create_guid(), owner_history, "Wall", "An awesome wall", None, wall_placement, product_shape, None)

# Define and associate the wall material
material = ifcfile.createIfcMaterial("wall material")
material_layer = ifcfile.createIfcMaterialLayer(material, 0.2, None)
material_layer_set = ifcfile.createIfcMaterialLayerSet([material_layer], None)
material_layer_set_usage = ifcfile.createIfcMaterialLayerSetUsage(material_layer_set, "AXIS2", "POSITIVE", -0.1)
ifcfile.createIfcRelAssociatesMaterial(create_guid(), owner_history, RelatedObjects=[wall], RelatingMaterial=material_layer_set_usage)

# Create and assign property set
property_values = [
    ifcfile.createIfcPropertySingleValue("Reference", "Reference", ifcfile.create_entity("IfcText", "Describe the Reference"), None),
    ifcfile.createIfcPropertySingleValue("IsExternal", "IsExternal", ifcfile.create_entity("IfcBoolean", True), None),
    ifcfile.createIfcPropertySingleValue("ThermalTransmittance", "ThermalTransmittance", ifcfile.create_entity("IfcReal", 2.569), None),
    ifcfile.createIfcPropertySingleValue("IntValue", "IntValue", ifcfile.create_entity("IfcInteger", 2), None)
]
property_set = ifcfile.createIfcPropertySet(create_guid(), owner_history, "Pset_WallCommon", None, property_values)
ifcfile.createIfcRelDefinesByProperties(create_guid(), owner_history, None, None, [wall], property_set)

# Add quantity information
quantity_values = [
    ifcfile.createIfcQuantityLength("Length", "Length of the wall", None, 5.0),
    ifcfile.createIfcQuantityArea("Area", "Area of the front face", None, 5.0 * solid.Depth),
    ifcfile.createIfcQuantityVolume("Volume", "Volume of the wall", None, 5.0 * solid.Depth * material_layer.LayerThickness)
]
element_quantity = ifcfile.createIfcElementQuantity(create_guid(), owner_history, "BaseQuantities", None, None, quantity_values)
ifcfile.createIfcRelDefinesByProperties(create_guid(), owner_history, None, None, [wall], element_quantity)

# Create and associate an opening for the window in the wall
opening_placement = create_ifclocalplacement(ifcfile, (0.5, 0.0, 1.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0), wall_placement)
opening_extrusion_placement = create_ifcaxis2placement(ifcfile, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
point_list_opening_extrusion_area = [(0.0, -0.1, 0.0), (3.0, -0.1, 0.0), (3.0, 0.1, 0.0), (0.0, 0.1, 0.0), (0.0, -0.1, 0.0)]
opening_solid = create_ifcextrudedareasolid(ifcfile, point_list_opening_extrusion_area, opening_extrusion_placement, (0.0, 0.0, 1.0), 1.0)
opening_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [opening_solid])
opening_shape = ifcfile.createIfcProductDefinitionShape(None, None, [opening_representation])
opening_element = ifcfile.createIfcOpeningElement(create_guid(), owner_history, "Opening", "An awesome opening", None, opening_placement, opening_shape, None)
ifcfile.createIfcRelVoidsElement(create_guid(), owner_history, None, None, wall, opening_element)

# Create a simplified representation for the Window
window_placement = create_ifclocalplacement(ifcfile, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0), opening_placement)
window_extrusion_placement = create_ifcaxis2placement(ifcfile, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
point_list_window_extrusion_area = [(0.0, -0.01, 0.0), (3.0, -0.01, 0.0), (3.0, 0.01, 0.0), (0.0, 0.01, 0.0), (0.0, -0.01, 0.0)]
window_solid = create_ifcextrudedareasolid(ifcfile, point_list_window_extrusion_area, window_extrusion_placement, (0.0, 0.0, 1.0), 1.0)
window_representation = ifcfile.createIfcShapeRepresentation(context, "Body", "SweptSolid", [window_solid])
window_shape = ifcfile.createIfcProductDefinitionShape(None, None, [window_representation])
window = ifcfile.createIfcWindow(create_guid(), owner_history, "Window", "An awesome window", None, window_placement, window_shape, None, None)

# Relate the window to the opening element
ifcfile.createIfcRelFillsElement(create_guid(), owner_history, None, None, opening_element, window)

# Relate the window and wall to the building storey
ifcfile.createIfcRelContainedInSpatialStructure(create_guid(), owner_history, "Building Storey Container", None, [wall, window], building_storey)

# Write the contents of the file to disk

# clear the existing data or write a new file if empty
# add your local file path here
file = open("hello_wall2.ifc","r+")
file. truncate(0)
file. close()

for thing in ifcfile:
    with open("C:/Users/admin-timmc/Desktop/blenderIFC example/hello_wall2.ifc", "r+") as file:
        content = file.read()
        file.seek(0)
        file.write(str(thing) + '\n'+ content)
        file.close()   


```

### Advanced Example 4
Define a class and function to load models (Hard)

For this example we will work with classes and functions to load the model, the reason for this is it will make it much more simple when we try and load multiple models in the next example. 

*This code include the import and model loading as it is a special case.*

```Python

import ifcopenshell
import ifcopenshell.geom

# we need this module to tell us how long our code took to run

import time
start_time=time.time()

# This is the tree settings - you shouldn't need to change this. keep it as is.
# it is a smart way to structure the geometry of the model, 
# so that we can do super fast 'bounding box' tests, where the 
# smallest possible box isnt drawn around the object.
# the we can then do fast clash detection on those boxes. 
# i.e. does the bounding box of the slab intersect the bounding box of any columns?

tree_settings = ifcopenshell.geom.settings()
tree_settings.set(tree_settings.DISABLE_OPENING_SUBTRACTIONS, True)

# This is a class, - your first one! good job! 
# it defines an object (Model) that has attributes (i.e. name)- cool eh?
# using this means we can get attribute info about the geometry model

class Model:
  def __init__(self,name, file, geometry, load_time):
    self.name = name
    self.file = file
    self.geometry = geometry
    self.load_time = load_time

# this is a function, we use functions when we want to repeat the same process in the code
# in python we need to define (def) the function before we can call it.
# we call the function below with model=getGeometry('ARCHI',f_ifc, tree_settings)
# the function makes an instance of the model class defined above and 'returns'
# this to us in.

def getGeometry(model_name,file,tree_settings):
    start_time=time.time()
    a = ifcopenshell.geom.tree()
    a.add_file(file, tree_settings)
    load_time = time.time()-start_time
    mod = Model(model_name,file,a,load_time)
    return mod

# now that we have done all that work above defining classes and functions,
# the code below can be quite simple (it is only 3 lines.
# you can see that it is important to name the functions and classes in a meaningful way to
# contribute to the legibility of your code.

f_ifc = ifcopenshell.open("model/Duplex_A_20110907_optimized.ifc")
f_geo = getGeometry('ARCHI',f_ifc, tree_settings)
print("\n\t{} Model took {:06.2f} seconds to load".format(f_geo.name,f_geo.load_time))

```
### Advanced Example 5a
Compare geometry in different models

This code enables you to load in different models into the same geometry model / tree (line 16). The arch model is added on line 20 and the MECH model is added on line 27. Line 31 and 32 define the Ifc classes that you will use for your clash detection, in this example we are identifying clashes between IfcSpace and IfcFlowSegment as the IfcFlowSegment is something that definitely appears in the MECH model.

*This code include the import and model loading as it is a special case.*

```Python
import ifcopenshell
import ifcopenshell.geom
import time

# setup
start_time=time.time()
tree_settings = ifcopenshell.geom.settings()
tree_settings.set(tree_settings.DISABLE_OPENING_SUBTRACTIONS, True)
    
# this gets the architectural model
a_ifc = ifcopenshell.open("model/Duplex_A_20110907_optimized.ifc")
# this gets the mechanical model
m_ifc = ifcopenshell.open("model/Duplex_M_20111024_optimized.ifc")

# this is a sperate geometry model tree
t = ifcopenshell.geom.tree()

start_time=time.time()
# this adds the architecture geometry to the tree
t.add_file(a_ifc, tree_settings)
load_time = time.time()-start_time
print("\n\t{} Model took {:06.2f} seconds to load".format('ARCH',load_time))

start_time=time.time()
# this adds the mechanical geometry to the tree
t.add_file(m_ifc, tree_settings)
load_time = time.time()-start_time
print("\n\t{} Model took {:06.2f} seconds to load".format('MECH',load_time))

total_clashes = 0
obj1 = "IfcSlab"
obj2 = "IfcFlowSegment"

start_time=time.time()

# ok so in this example I want to take
clashed = a_ifc.by_type(obj1)
for clash_object in clashed:
    #print('### {}'.format(space.Name))
    for obj in t.select_box(clash_object):
        if (obj.is_a(obj2)):
            #print ('\t  - {}'.format(obj.Name))
            total_clashes+=1
print("\n\tTotal clashes between {} and {} : {:6} ".format(obj1,obj2,total_clashes))
load_time = time.time()-start_time
print("\n\tClash detection took {:06.6f} seconds to complete".format(load_time))

```
### Advanced Example 5b
Other collision functions to explore

Extend the previous examples with the following commands ….

```Python
# extend the bounding box of the object being tested -> wall in this case
t.select_box(wall, extend=1.)

# extend the bounding box of the object being tested 
# and state that it has to be completely inside
t.select_box(wall, extend=0.001, completely_within=True)

# get the geometry in t that clash with point 0,0,0
t.select((0.,0.,0.))

# get the geometry in t that intersect a bounding box defined by (-1.,-1.,-1.) -> (1.,1.,1.)
t.select_box(((-1.,-1.,-1.),(1.,1.,1.)))

# get the t geometry that intersect a bounding box defined by (-2.,-2.,-2.) -> (10.,10.,10.)
# and is completely contained by it
t.select_box(((-2.,-2.,-2.),(10.,10.,10.)), completely_within=True)
```
### Advanced Example 6
Super fast property queries using selector (Currently working on this)

Ok, so this is pretty straight forward, the only thing that might mess this is up, is that selector has a dependency called lark, to install lark you can follow the guide here. Or if feeling brave, just get the command line open and type:

>pip install lark-parser --upgrade

![image](https://github.com/timmcginley/41934/assets/1415855/3613f2f4-38a4-4c79-b6e9-45ed5e929626)


You can look at the code examples here, to see what would be possible with it.
Examples for how to use it:

```Python

#import the module and setup
import ifcopenshell.util
from ifcopenshell.util.selector import Selector
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')
 selector = Selector()

#this is equivalent to model.by_type(‘IfcWallStandardCase’)
walls = selector.parse(model, '.IfcWallStandardCase')
 print(walls)
 noWalls = len(walls)
 print("There are {} walls in the model".format(noWalls)) 
#this is equivalent to searching by GlobalId
wall = selector.parse(model, '.IfcWallStandardCase'[GlobalId = "2O2Fr$t4X7Zf8NOew3FLOH"]') 
 print(wall)

#you can search for elements based on their properties
#here you find all the external walls
extWalls = selector.parse(model, '.IfcWallStandardCase'[Pset_WallCommon.IsExternal = "True"]')
 noExtwalls = len(extWalls)
 print("There are {} external walls in the model".format(noExtwalls))

#here you find all the spaces on level 1
spaces = selector.parse(model, '.IfcSpace[PSet_Revit_Constraints.Level = "Level 1"]')
 noSpaces = len(spaces)
 print("There are {} spaces on level 1".format(noSpaces))

#find all walls with a volume above 5
wallsVol = selector.parse(model, '.IfcWallStandardCase[PSet_Revit_Dimensions.Volume > "5"]')
 noWallsVol = len(wallsVol)
 print("{} walls out of {} walls in the model have a volume above 5".format(noWallsVol,noWalls))
```
### Advanced Example 7a
Check the NUMBER of stories in different models

This example checks to see if different models have the same number of stories. 

*This code include the import and model loading as it is a special case.*

```Python
import ifcopenshell
    
# this gets the architectural model
a_ifc = ifcopenshell.open("model/Duplex_A_20110907_optimized.ifc")
# this gets the mechanical model
m_ifc = ifcopenshell.open("model/Duplex_M_20111024_optimized.ifc")

# Ok so above we loaded 2 models...
a_stories = a_ifc.by_type('IfcBuildingStorey')
m_stories = m_ifc.by_type('IfcBuildingStorey')

# first we need to check if they have the same number of stories
# check to see if the number of stories is the same in the different models...
if (len(a_stories) == len(m_stories)):
    print ('\n\tnumber of stories matches')
    
# else if that is not true ... is a BIGGER than m ...
elif (len(a_stories) > len(m_stories)):
    print ('\n\tmodel_a has more stories than model_b')
    
# else if that is not true ... is a SMALLLER than m ...
elif (len(a_stories) < len(m_stories)):
    print ('\n\tmodel_a has less stories than model_b')

```
### Advanced Example 7b
Compare the storey ELEVATIONS in different models 

We use a while loop here which iterates through the len of a_stories. This could cause a problem if there are less b_stories than a_stories. So we use the try command here, this enables us to try a piece of code, and if it doesn’t work it will trigger except, and enable us to define an error message to help us debug our program or provide feedback to the user.

*This code include the import and model loading as it is a special case.*

```Python
import ifcopenshell   
# this gets the architectural model
a_ifc = ifcopenshell.open("model/Duplex_A_20110907_optimized.ifc")
# this gets the mechanical model
m_ifc = ifcopenshell.open("model/Duplex_M_20111024_optimized.ifc")

# Ok so above we loaded 2 models...
a_stories = a_ifc.by_type('IfcBuildingStorey')
m_stories = m_ifc.by_type('IfcBuildingStorey')
# we are creating a counter here to help us iterate through the stories
count = 0
# we use a while loop here
while count < len(a_stories):
    # try is really cool and stops your code blowing up!
    try:
        print ('for {} level: a is at {:04.2f} m, and b is at {:04.2f} m'.format(count,a_stories[count].Elevation,m_stories[count].Elevation))
        # each time this loop runs it adds one to count and gets 
        # closer to the len of m_stories 
    except:
        print ('something went wrong')
count+= 1     
```
### Advanced Example 7c
Are the ELEVATIONS in diff models the same?

This example is a combination of the logic in 7a and 7b

*This code include the import and model loading as it is a special case.*

```Python
 
import ifcopenshell   
# this gets the architectural model
a_ifc = ifcopenshell.open("model/Duplex_A_20110907_optimized.ifc")
# this gets the mechanical model
m_ifc = ifcopenshell.open("model/Duplex_M_20111024_optimized.ifc")

# Ok so above we loaded 2 models...
a_stories = a_ifc.by_type('IfcBuildingStorey')
m_stories = m_ifc.by_type('IfcBuildingStorey')

# we are creating a counter here to help us iterate through the stories
count = 0

# we use a while loop here
while count < len(a_stories):
    # try is really cool and stops your code blowing up!
    try:
        # here we grab the elevations and also round them up to 3 decimal places
        a_elev= round(a_stories[count].Elevation,3)
        m_elev= round(m_stories[count].Elevation,3)
        # we can then print the elevations as we did in example 7A
        print ('\n[{} level] a : {:04.3f}m | b : {:04.3f}m'.format(count,a_elev,m_elev))
        # test if the rounded values are equal
        if (a_elev == m_elev):
            print ('- PASS these match!')
        else:
            print ('- FAIL these do not match')
    except:
        print ('\nError: maybe one of the models ran out of floors?')
    count+= 1 
```
Example output from 7c - does this match what you got? - why does it error? is the answer in 7a?!?
![image](https://github.com/timmcginley/41934/assets/1415855/8b76f696-8371-4d31-b838-ab556bf43132)


### Advanced Example 8a
Property check

Description and comments to follow.

```Python

for entity in model.by_type("IfcFooting"): 
    ele_at_bottom = False
    #we need to get the attributes 
    for relDefinesByProperties in entity.IsDefinedBy: 
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties: 
            #and then get the attribute we are looking for 
            if prop.Name == 'Elevation at Bottom': 
                #add the length to the total length 
                ele_at_bottom = True
    
    if (ele_at_bottom):
        print ('[X] {}'.format(entity.Name))
    else:
        print ('[ ] {}'.format(entity.Name)) 
```
### Advanced Example 8b
Generic Property list

OK so this is my best bet its not perfect but you should be able to adapt it to your needs and it works for windows and doors 😊

```Python

print ('\n## search all properties of a type ##\n')

# lets search all property sets           
for pset in model.by_type("IfcPropertySet"): 
    # and all single values within those property sets (that have props)
    for prop in pset.HasProperties:
        # and check if that property matches the one we are looking for...
        if prop.is_a("IfcPropertySingleValue"):
            obj = model.get_inverse(pset)
            # ok cool so now get the related objects
            # so then we get the entity related to that property
            for part in obj[0].RelatedObjects:
                # then we check if the entity is a window
                if (part.is_a('IfcWindow')):
                    # print the property sets that you have found
                    print ('{} : {}'.format(prop.Name,prop.NominalValue.wrappedValue)) 

```
### Advanced Example 8c
Find entities based on a singlevalue property

I think this one is pretty cool, I was trying to write an example for 8b and ended up with this. The logic is that we  define  the property and value we are looking for , get it and then seeks its inverse entities. 

```Python

propName ='Unbounded Height'
value= 2.6

print ('\n## search entity by property and value ##\n')
print ('Searching for...')
print ('\tIfcPropertySingleValue = [ {} : {} ]'.format(propName,value))

# lets search all property sets
count = 0
print ('Results:')
            
for pset in model.by_type("IfcPropertySet"): 
    # and all single values within those property sets (that have props)
    for prop in pset.HasProperties:
        # and check if that property matches the one we are looking for...
        if prop.is_a("IfcPropertySingleValue") and prop.Name == propName and prop.NominalValue.wrappedValue == value:
            # then get the objects inverse relations
            obj = model.get_inverse(pset)

            # ok cool so now get the related object …
            for part in obj[0].RelatedObjects:
                
                print('\t# {:3} | {:12} | {}'.format(count,part.Name,part.GlobalId))
                count+=1
```
![image](https://github.com/timmcginley/41934/assets/1415855/766062d9-9bab-4120-87a2-5aae71a8e4cf)


[entities]: /41934/Concepts/Entities
[use]: /41934/Uses
[IDE]: /41934/Concepts/IDE

## Glossary of terms (Work in progress)
Format - we use this to make the output statements pretty and reduce the amount of logic that we need to include in the print statement -> check it out here https://pyformat.info/
Example
```Python
print('-\t{}'.format(obj.Name))
```
Input - Get more information -> https://www.w3schools.com/python/ref_func_input.asp
	Example
	print

Function - sometimes we might have to define a function for code that we will reuse in our script for instance https://www.tutorialspoint.com/python/python_functions.htm



