## BlenderBIM

BlenderBIM solves the problem of expensive, siloed, segmented, differentiated software written in different native models that then need to be converted to other models in order to collaborate.

BlenderBIM is free, open source, native IFC authering platform based on the IfcOpenShell library. It's a plugin to the open source modelling and render software [Blender](https://www.blender.org/). Blender has been open source since [2002](https://www.blender.org/about/history/#:~:text=On%20Sunday%2C%20October%2013th%2C%202002,used%20for%20any%20purpose%20whatsoever.). BlenderBIM enables BIM modelling natively in IFC wch is not possible in any other BIM software.

The problem with traditional proprietary BIM tools is that it is not possible to read the source code of the tools to find out how they really work. Furthermore developing tools for them is difficult because they can change how they work between the versions. The business model is to frequently ship new versions of many different software which is expensive, frustrating and makes existing silos in the AEC worse.


<!-- Exercise - please do videos 1 - 5 from [this set of tutorials] (https://osarch.org/2022/11/12/%f0%9f%93%ba-ifc-101-a-free-ifc-crash-course-with-python/) from the awesome Yassine Oualid. -->

## Tutorials and resources:

### Beginner
- The [OSArch wiki](https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on) is generally a good resource on BlenderBIM, IfcOpenShell and OpenBIM in general.
- [BlenderBIM full free course](https://www.youtube.com/watch?v=pjO_Nh6yaYw&list=PLbFY94gzUJhGXh9tEZIuq-a8BSWddSPz2) from scratch to pro
- [Exploring IFC model](https://docs.bonsaibim.org/users/quickstart/explore_model.html)
- Great starting point - [Using BlenderBIM with native IFC](https://www.youtube.com/watch?v=Ooh05WF__80&ab_channel=DionMoult)
- Check out tutorials from [Ifc Architect](https://www.youtube.com/@IfcArchitect/videos)
- [Adding information to an IFC model](https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on_adding_information_to_IFC)
### Coding in BlenderBIM
- [Using the Python console with BlenderBIM add-on](https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on/Using_the_Python_console_with_BlenderBIM_Add-on)
- [How to run an external script in Blender](https://github.com/timmcginley/41934/blob/main/Concepts/BlenderBIM/E22_41934_How%20to%20run%20an%20external%20script%20in%20Blender.md)
- [BlenderBIM code examples](https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on/BlenderBIM_Add-on_code_examples)


## BlenderBIM 
Following a brief introduction, we will look at the following steps.

* [Install Blender](https://docs.bonsaibim.org/users/quickstart/installation.html)
* [Install BlenderBIM](https://docs.bonsaibim.org/users/quickstart/installation.html)
* Grab an example IFC model from the IFC Models folder
* If you follow this tutorial, you'll get a brief introduction to Blender and BlenderBIM 
Explore that IFC model. Can you find:

* the number of spaces in the building?
* the number of levels?
* the materials in the building?
* the area of the floors?

After this, we will introduce the scripting environment in Blender to speed up these checks.

## Scripting IfcOpenShell in Blender
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
You can have a look at [this](https://docs.ifcopenshell.org/ifcopenshell-python/hello_world.html) IfcOpenShell crash course for more examples. What other information can you find out about the model?

Finally, you can get (if you don't have one already) a Github account for your group (this can be your normal account) and create a repository for the course, so it will be ready for you to add scripts to in the following weeks.

