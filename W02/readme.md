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

