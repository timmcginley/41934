# Python / IfcOpenShell

## Python basics

There are lots of good places to learn python but [this one](https://www.learnpython.org/) looks fun and interactive.

## Python in Blender 

Please check out [c-claus](https://github.com/C-Claus/BlenderScripts)'s python blender scripts. Also this [video](https://www.youtube.com/watch?v=8835RgwH-pM&ab_channel=C.Claus)

## IfcOpenShell Examples(what we use most)

>these scripts need you to import ifcopenshell and load the model first...



* N.B. in these examples for consistency we name the model 'model'. if you are suing somethign different that is ok, but the idea here is to keep the code consistent to help you.

* LOADING AND IMPORTING IFFOPENSHELL DEPENDS ON YOUR ENVIRONMENT:

1. If in Blender do....

```python
import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')
```

3. If in the console / terminal do...

```python
import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')
```

Rule: Check the number of spaces in the model

### Example 1a: 
loop through the [entities] and then add one to the variable *spaces_in_model* each time we find an instance of that entity.

```python
import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')

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

### Example 1b: 
Use len() to count the number of [entities] (without having to loop through all of them).

```python

import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')

spaces_required = 21
spaces_in_model = len(model.by_type("IfcSpace"))

print("\nThere are "+str(spaces_in_model)+" spaces in the model")

if (spaces_required == spaces_in_model):
    print ('RESULT: The number of spaces is correct')
else:
    print ('RESULT: The number of doors is wrong')
```

Rule: In this example we will try to quantify the length of the beam. We will base this on the for loop we defined in example 1A.

### Example 2: 
Quantify [use] case code example

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

## Advanced Python Scripts

### Example 1: 
Get the property sets of an element

```Python
# ########### this is required if running from console ############

import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')

# ########### end of required if running from console #############

# ############## code below needed in both cases ##################

# this just gets you the entity, defined here as wall
# feel free to change this to your needs
wall = model.by_type('IfcWall')[0]
for definition in wall.IsDefinedBy:
	# To support IFC2X3, we need to filter our results.
	if definition.is_a('IfcRelDefinesByProperties'):
		property_set = definition.RelatingPropertyDefinition
		# Might return Pset_WallCommon
		print(property_set.Name)

# ###################### end of example ###########################
```
Example 2: 
Get the doors that bound a space (BoundedBy) 

This example works to get you the doors (line 13) that bound the space (line 8)

```Python
# ########### this is required if running from console ############
import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')

for space in model.by_type("IfcSpace"):
    near = space.BoundedBy
    print("\n\t####{}\n".format(space.Name))
    for objects in near:
        if (objects.RelatedBuildingElement != None):
            if (objects.RelatedBuildingElement.is_a('IfcDoor')):
                print(objects.RelatedBuildingElement.Name)

# ###################### end of example ########################### 
```
### Example 3: 
Get the doors that bound a space (BoundedBy)

For this example we have to include an additional library, but it provides a really cool approach. Also please note that this example uses the optimized version of the Duplex model. This is also available in your models folder. Optimised versions of files are much smaller, they are optimized using a great tool (Solibri IFC Optimizer) from Solibri. The idea is that it can be used to make IFC files easier to share.
```Python
# We need all this code and we can’t run it from RWTH viewer
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
### Example 4: 
Define a class and function to load models (Hard)

For this example we will work with classes and functions to load the model, the reason for this is it will make it much more simple when we try and load multiple models in the next example. 

```Python
# We need all this code and we can’t run it from RWTH viewer

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
### Example 5: 
Compare geometry in different models

This code enables you to load in different models into the same geometry model / tree (line 16). The arch model is added on line 20 and the MECH model is added on line 27. Line 31 and 32 define the Ifc classes that you will use for your clash detection, in this example we are identifying clashes between IfcSpace and IfcFlowSegment as the IfcFlowSegment is something that definitely appears in the MECH model.


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
### Example 5a: 
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
### Example 6: 
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
### Example 7a: 
Check the NUMBER of stories in different models

This example checks to see if different models have the same number of stories. 
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
### Example 7b: 
Compare the storey ELEVATIONS in different models 

We use a while loop here which iterates through the len of a_stories. This could cause a problem if there are less b_stories than a_stories. So we use the try command here, this enables us to try a piece of code, and if it doesn’t work it will trigger except, and enable us to define an error message to help us debug our program or provide feedback to the user.

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
Example 7c: 
Are the ELEVATIONS in diff models the same?

This example is a combination of the logic in 7a and 7b
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


### Example 8a: 
Property check

Descirption and comments to follow
```Python
import ifcopenshell
model = ifcopenshell.open("model\Duplex_A_20110907.ifc")

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
### Example 8b: 
Generic Property list

OK so this is my best bet its not perfect but you should be able to adapt it to your needs and it works for windows and doors 😊

```Python
import ifcopenshell
model = ifcopenshell.open("model\Duplex_A_20110907.ifc")

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
### Example 8c: 
Find entities based on a singlevalue property

I think this one is pretty cool, I was trying to write an example for 8b and ended up with this. The logic is that we  define  the property and value we are looking for , get it and then seeks its inverse entities. 

```Python
import ifcopenshell
model = ifcopenshell.open(" model\Duplex_A_20110907.ifc")

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


### Example 9a: 
Door code check

This is an edit of Kallina’s door code check, its a good example. 
```Python
import ifcopenshell 
model = ifcopenshell.open("model\Duplex_A_20110907.ifc")  
 
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


[entities]: /41934/Concepts/Entities
[use]: /41934/Uses

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


