## Tutorials

Exercise - please do videos 1 - 5 from [this set of tutorials](https://osarch.org/2022/11/12/%f0%9f%93%ba-ifc-101-a-free-ifc-crash-course-with-python/)


- [video] [BlenderBIM full free course](https://www.youtube.com/watch?v=pjO_Nh6yaYw&list=PLbFY94gzUJhGXh9tEZIuq-a8BSWddSPz2) from scratch to pro
- How to run an external script in Blender: https://github.com/timmcginley/41934/blob/main/Tutorials/E22_41934_How%20to%20run%20an%20external%20script%20in%20Blender.md
- Exploring IFC model: https://blenderbim.org/docs-python/ifcopenshell-python/hello_world.html
- My first BIM project: https://blenderbim.org/blenderbim-tutorial.html
- Using the Python console with BlenderBIM add-on: https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on/Using_the_Python_console_with_BlenderBIM_Add-on
- BlenderBIM code examples: https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on/BlenderBIM_Add-on_code_examples

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

