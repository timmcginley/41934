# How to run an external script in Blender
## To view outputs of your file
The outputs (eg. print statements) of your file won't show in the Blender console. They are output to the system console (your computers terminal/command prompt).
### Windows
On Windows you can open the system console by simply clicking "Window -> Toggle System Console"

![Alt text](./images/Pasted%20image%2020220912133739.png?raw=true)
### MacOS/Linux
On MacOS or Linux systems you have to run Blender from the terminal to be able to see outputs.

- Open your terminal and navigate to Blender location. This will typically be at `/Applications/Blender.app/Contents/MacOS`
- Go to this location with the command `cd` (change directory) as:
	`cd /Applications/Blender.app/Contents/MacOS`
- Run Blender by typing:
	`./Blender`
	Blender will open up as normally. Now, whenever you run your script, the outputs will be shown here.

![Alt text](./images/Screenshot%202022-09-12%20at%2013.29.30.png?raw=true "Title")
## Running an external script
### Open Blender (either normally or through a terminal) and make a new 'text' window.

![Alt text](./images/Screenshot%202022-09-12%20at%2014.25.49.png?raw=true "Title")
### (A) If you want to use the IFC model through in Blender
#### Load it with BlenderBIM

![Alt text](./images/Screenshot%202022-09-12%20at%2013.21.39%201.png?raw=true "Title")

![Alt text](./images/Screenshot%202022-09-12%20at%2013.22.05.png?raw=true "Title")
#### Test file
- Make a new `hello_ifc.py` file and place it in the same directory as your blender file.

```python
# IF YOU'RE USING THE IFC MODEL LOADED IN BLENDER
from blenderbim.bim.ifc import IfcStore

file = IfcStore.get_file()
spaces = file.by_type("IfcSpace")

for space in spaces:
	print(space.LongName)
```

### (B) If you want to use another, external IFC model 
- Place both the IFC model  and a new `hello_ifc.py` in the same directory as your blender file
#### Test file
```python
# IF YOU'RE ANOTHER, EXTERNAL IFC MODEL
import ifcopenshell
import bpy
import os


modelname = "Duplex_A_20110907.ifc"
modelpath = os.path.join(os.path.dirname(bpy.data.filepath), modelname)
file = ifcopenshell.open(modelpath)

spaces = file.by_type("IfcSpace")

for space in spaces:
	print(space.LongName)
```

### Open template for external scripts
![Alt text](./images/Screenshot%202022-09-12%20at%2013.22.44.png?raw=true "Title")
### Change filename to your file name (eg. "hello_ifc.py")
![Alt text](./images/Screenshot%202022-09-12%20at%2013.23.09.png?raw=true "Title")
### Run your script
![Alt text](./images/Screenshot%202022-09-12%20at%2014.10.58.png?raw=true "Title")
Your system console should be showing a list of space names.
![Alt text](./images/Screenshot%202022-09-12%20at%2013.24.23.png?raw=true "Title")
