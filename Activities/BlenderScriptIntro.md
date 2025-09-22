# Blender Scripting introduction with Bonsai
In the previous activity we found information about our IFC model in the properties tabs of Blender. We found that it could be tricky to find information quickly, for instance how many windows are in the model? Therefore in this example we will use some simple scripting to answer these questions.

## Activity Summary
Specifically in this activity you will learn:
1. Where to find the script window in Blender
2. How to import the [IfcOpenShell] [python] library
3. How to load the model in Python
4. How to query an Ifc Entity
5. How to find how many instances of that entity are in you model
6. How to print that to console window (and where to fin the console window)

## Activity Steps
We will repeat some of these steps in the next activity where we work with Python outside of Blender directly in an [IDE] or in the [console].

### Load your IFC model in Blender
* Make sure you have already loaded your IFC model in Blender and can see it in the 3d window. Please choose the model that you think you can find your focus information on.

### Open the Blender script window
* From the top menu bar of Blender click the scripting tab
* Before you can start scripting you need to make a new script from the tab in the scripting window
> N.B. In order to see the output of your script in windows you need to click 'Window > Toggle System Console'

## Your first code
* We know some of you are a little nervous about programming, but when we start we only need to know 2 things - copy and paste :)
* So that we can reuse code as much as possible, python uses existing libraries of code. It lets you import these libraries into your script. Later you will learn how to mkae your own library but in this course we will always first import the [ifcopenshell] library.
* You are now working in Python, the first thing we need to do is import the python library we are working with in this course - [ifcOpenShell]
* Next we get the current model from blender BIM.
* To do this copy and paste the code below into your Blender Scriping window:

```python
import ifcopenshell
```
* Next add this line that imports the current IFC model from blender. We only need this when working inside Blender, please make sure it says bonsai.bim.ifc and not blenderBIM.bim.ifc, many examples you find online will still use the old name of the library.

```python
from bonsai.bim.ifc import IfcStore
```

* Now you can add get the IFC file that is active in your Blender environment with:
```python
file = IfcStore.get_file()
```
* Cool now we can access the IFC file :)

* You will be looking for a different entity in this exercise i.e
  * Architecture IFC model - IfcWindow / IfcDoor
  * Structure IFC model - IfcBeam / IfcColumn
  * MEP IFC model - IfcDuctSegment

Therfore, only choose one of the 3 lines of code below.
* We will use the variable **things** normally we would call it something more specific but in this exercise you need to choose which line to copy. You can think of **things** as a box that containing all the instances of the entity you are interested in, cool eh?

### Architecture model
* To get all the windows from the architecture model type:
```python
things = file.by_type('IfcWindow')
```
### Structure model
* Or to get all the columns from the structure model type:
```python
things = file.by_type('IfcColumn')
```
### MEP model
Or get all the ducts from the MEP model type:
```python
things = file.by_type('IfcDuctSegment')
```
### Check how many of the thing you have
Now that you have checked for your things.
Get Python to tell us how many of the thing you have with the len() function.
*Also you will see that this is contained in a print() function, this is pythons way of reporting information back to the console so you can see the answer.
* So lets go ahead and check how many of your chosen things your model has ...
```python
print(len(things))
```
or print their names...
```python
for thing in things:
	print(thing.LongName)
```
You can have a look at [this](https://docs.ifcopenshell.org/ifcopenshell-python/hello_world.html) IfcOpenShell crash course for more examples. What other information can you find out about the model?7

[IfcOpenShell]: /Concepts/IfcOpenShell.md
[IDE]: /Concepts/IDE.md
[console]: /Concepts/CommandLine.md
