# IfcOpenShell Examples

```{toctree}
:hidden:
:glob:
*
*/index
```

**N.B.!** IfcOpenShell is a library for Python and thus follows the logic and syntax of the language. Having at least some basic knowledge of Python will make scripting with IfcOpenShell much easier and less confusing. If you don't have any experience with Python, doing some exercises from a tutorial site like  [codecademy](https://www.codecademy.com/catalog/language/python "https://www.codecademy.com/catalog/language/python") or  [freecodecamp](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/ "https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/") is strongly recommended. 

You can also start with [this tutorial](https://github.com/jakob-beetz/ifcopenshell-notebooks) on IfcOpenShell, as it also includes a crash course on Python. If you are already familiar with Python, you can jump to file 04_hello_ifc. This tutorial is made as Jupyter notebooks and doesn't require you to install anything, simply click on the button **"launch | binder"** at the top of the README.md and wait for it to load. (If the binder isn't working, you can check out [this wiki](https://github.com/jakob-beetz/IfcOpenShellScriptingTutorial/wiki), which has the same content. Just copy the code snippets to your code editor.)

Other excellent beginner tutorials and recourses on IfcOpenShell:
- IfcOpenShell "Hello, world!" https://blenderbim.org/docs-python/ifcopenshell-python/hello_world.html (strongly recommended)
- IfcOpenShell Code examples https://blenderbim.org/docs-python/ifcopenshell-python/code_examples.html. The first ones are beginner-friendly and increase in difficulty. A good resource for your projects.
- Some more IfcOpenShell code examples https://wiki.osarch.org/index.php?title=IfcOpenShell_code_examples#Geometry_processing
-  BlenderBIM code examples https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on/BlenderBIM_Add-on_code_examples
- IFC-101 – A Free IFC crash course with Yassine: https://osarch.org/2022/11/12/%f0%9f%93%ba-ifc-101-a-free-ifc-crash-course-with-python/. (you can focus on Episode 03-05B)

Below are small scripts and snippets that we've used over the run of this course. Try them out for yourself!

* N.B. in these examples for consistency we name the model 'model'; if you are using somethign different that is ok, but the idea here is to keep the code consistent to help you.

## Loading and importing the model and IfcOpenShell into the code editor you are using

If you are in Blender and want to use the IFC model you have open in the model view:

```python

import bpy
from blenderbim.bim.ifc import IfcStore
model = IfcStore.get_file()

```
If you are in an external code editor, terminal OR you are in Blender, but you want to use a different IFC model than the one you have loaded:

*N.B. please change the model for the one you are using :)*

```python
import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')
```

## [Basic Scripts](/41938/Examples/IfcOpenShell/Basic)
## [Intermdiate Scripts](/41938/Examples/IfcOpenShell/Intermediate)
## [Advanced Scripts](/41938/Examples/IfcOpenShell/Advanced)


[entities]: /41934/Concepts/Entities
[use]: /41934/Uses
[IDE]: /41934/Concepts/IDE





