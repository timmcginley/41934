# Basic IfcOpenshell Examples

* N.B. in these examples for consistency we name the model 'model'; if you are using somethign different that is ok, but the idea here is to keep the code consistent to help you.

## Introduction 

Loading and importing the model and ifcOpenShell into the [IDE] you are using

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
