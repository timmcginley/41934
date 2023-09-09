# IfcOpenShell Examples

* N.B. in these examples for consistency we name the model 'model'; if you are using somethign different that is ok, but the idea here is to keep the code consistent to help you.

## Loading and importing the model and ifcOpenShell into the [IDE] you are using

If in Blender do....

```python

import bpy
from blenderbim.bim.ifc import IfcStore
model = IfcStore.get_file()

```

If in the console / terminal do... 
*N.B.please change the model for the one you are using :)*

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





