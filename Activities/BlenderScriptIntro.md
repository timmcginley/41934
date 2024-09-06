# Blender Scripting introduction with Bonsai

## Activity Summary
In this activity you will learn:
* Where to find the script window in Blender
* How to import the [IfcOpenShell] [python] library
* How to load the model in Python
* How to query an Ifc Entity
* How to find how many instances of that entity are in you model
* How to print that to console window (and where to fin the console window)

## Activity Steps
We will repeat some of these steps in the next activity where we work with Python outside of Blender directly in an [IDE] or in the [console].

### first, load an IFC model through the File menu on the main toolbar
* This exercise works best with the architecture model as we will be trying to find the spaces in the model.

### Open the Blender script window
* From the top menu bar of Blender click the scripting tab
* Before you can start scripting you need to make a new script from the tab in the scripting window
> N.B. In order to see the output of your script in windows you need to click 'Window > Toggle System Console'

## Your first code
1. We know some of you are a little nervous about programming, but when we start we only need to know 2 things - copy and paste :)
1. So that we can reuse code as much as possible, python uses existing libraries of code. It lets you import these libraries into your script. Later you will learn how to mkae your own library but in this course we will always first import the [ifcopenshell] library.
1. You are now working in Python, the first thing we need to do is import the python library we are working with in this course - [ifcOpenShell]
1. Next we get the current model from blender BIM.
1. To do this copy and paste the code below into your Blender Scriping window:

```python
import ifcopenshell
```
1. Next add this line that imports the current IFC model from blender. We only need this when workign inside Blender, please make sure it says bonsai.bim.ifc and not blenderBIM.bim.ifc, many examples you find online will still use the old name of the library.

```python
from bonsai.bim.ifc import IfcStore
```

Now you can add get the IFC file that is active in your Blender environment with:
```python
file = IfcStore.get_file()
```
Cool now we can access the IFC file :)

You can get all the spaces in your file by:
```python
spaces = file.by_type('IfcSpace')
```
Now check how many spaces you have...
```python
print(len(spaces))
```
or print their names...
```python
for space in spaces:
	print(space.LongName)
```
You can have a look at [this](https://docs.ifcopenshell.org/ifcopenshell-python/hello_world.html) IfcOpenShell crash course for more examples. What other information can you find out about the model?7

[IfcOpenShell]: /Concepts/IfcOpenShell
[IDE]: /Concepts/IDE
[console]: /Concepts/CommandLine
