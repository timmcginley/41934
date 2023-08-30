# Advanced IfcOpenShell

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

## Advanced Examples

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




