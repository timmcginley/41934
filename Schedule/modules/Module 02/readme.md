# Classification

There are many different types of classification in BIM. In this session we will try to map the elements we identify in the Duplex model to 2 different classification systems.

## BlenderBIM 
Following a brief introduction, we will look at the following steps.

* [Install Blender](https://blenderbim.org/docs/users/installation.html)
* [Install BlenderBIM](https://blenderbim.org/docs/users/installation.html)
* Grab an example IFC model from the IFC Models folder
* If you follow this tutorial, you'll get a brief introduction to Blender and BlenderBIM 
Explore that IFC model. Can you find:

1. the number of spaces in the building?
1. the number of levels?
1. the materials in the building?
1. the area of the floors?

After this, we will introduce the scripting environment in Blender to speed up these checks.

## Blender scripting environment

To set up the scripting environment, make a new Blender window and switch to Python console mode. Once you have done that, import the libraries by typing:

```python
import ifcopenshell
from blenderbim.bim.ifc import IfcStore
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
len(spaces)
```
or print their names...
```python
for space in spaces:
	print(space.LongName)
```
You can have a look at this IfcOpenShell crash course for more examples. What other information can you find out about the model?

Finally, you can get (if you don't have one already) a Github account for your group (this can be your normal account) and create a repository for the course, so it will be ready for you to add scripts to in the following weeks.

