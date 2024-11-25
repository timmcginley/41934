# Develop your own script

Now you can begin to develop an [IfcOpenShell] script.

[This activity needs to be updated]

Insert this piece of code at the beginning of your script. It solves the issue of different path syntax on different operating systems etc.
The only thing you have to do is to place your IFC model in a folder called `model` in the same place as your Python script.

```
main folder
├── your_script.py
├── model
│   ├── your_model.ifc
```
Change `modelname` to the name of your IFC model (notice no .ifc at the end!)

```python
from pathlib import Path
import ifcopenshell

modelname = "AC20-FZK-Haus2"

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: please check your model folder : {model_url} does not exist")

# Your script goes here

# Test if everything works:
spaces = model.by_type("IfcSpace")
for space in spaces:
    print(space.LongName)
```

## Activity Completion

### 01 Your tool - A Python script
* Your `main.py` tool including the code snippet from above. You can have multiple Python files, but then they should be imported into the `main.py` script.

### 02 The IFC model
* A `model` folder with a .ifc file inside of it. You can also have multiple IFC models placed here.
