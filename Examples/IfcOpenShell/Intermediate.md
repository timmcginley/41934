# Intermediate IfcOpenShell

* N.B. in these examples for consistency we name the model 'model'; if you are using somethign different that is ok, but the idea here is to keep the code consistent to help you.

## Intermediate examples
- Using IfcOpenShell to parse IFC files with Python - [https://thinkmoult.com/using-ifcopenshell-parse-ifc-files-python.html](https://thinkmoult.com/using-ifcopenshell-parse-ifc-files-python.html)

## Loading and importing the model and IfcOpenShell into the [IDE] you are using

If you are in Blender and want to use the IFC model you have open in the model view:

```python
import bpy
from blenderbim.bim.ifc import IfcStore
model = IfcStore.get_file()
```

If you are in an external code editor, terminal OR you are in Blender, but you want to use a different IFC model than the one you have loaded:

```python
import ifcopenshell
model = ifcopenshell.open('model\Duplex_A_20110907.ifc')
```

## Intermediate Examples
* [Intermediate 1 - Get doors that bound a space (BoundedBy)](#Intermediate-Example-1) - check!
* [Intermediate 2 - Get doors that bound a space (BoundedBy)](#Intermediate-Example-2) - is repeat?
* [Intermediate 3 - Open a file with a window using TKinter](#Intermediate-Example-3)
* [Intermediate 4A - Write data to excel files](#Intermediate-Example-4a)
* [Intermediate 4B - Write ifc data to excel files](#Intermediate-Example-4b)
* [Intermediate 4C - Write ifc data to excel files (in a function)](#Intermediate-Example-4c)
* [Intermediate 5A - read data from excel files](#Intermediate-Example-5a)
* [Intermediate 5B - read data from excel file and IFC file](#Intermediate-Example-5b)
* [Intermediate 6 - tKinter GUI](#Intermediate-Example-6)

### Intermediate Example 1 
Get the doors that bound a space (BoundedBy) 

This example works to get you the doors (line 13) that bound the space (line 8).

*remember to import ifcopenshell and load the model if you need to, see the [introduction](#Introduction) of this concept for more information.*

```Python
for space in model.by_type("IfcSpace"):
    near = space.BoundedBy
    print("\n\t####{}\n".format(space.Name))
    for objects in near:
        if (objects.RelatedBuildingElement != None):
            if (objects.RelatedBuildingElement.is_a('IfcDoor')):
                print(objects.RelatedBuildingElement.Name)
```

### Intermediate Example 2
Get the doors that bound a space (BoundedBy)

For this example we have to include an additional library, but it provides a really cool approach. Also please note that this example uses the optimized version of the Duplex model. This is also available in your models folder. Optimised versions of files are much smaller, they are optimized using a great tool (Solibri IFC Optimizer) from Solibri. The idea is that it can be used to make IFC files easier to share.

*This code includes the import and model loading as it is a special case.*

```Python
import ifcopenshell
# That was normal the new bit is this geom lib below
import ifcopenshell.geom
# ok, so we are calling it fn (for file name here) - lets stick to that
fn = "model/Duplex_A_20110907_optimized.ifc"

# based on the fn we can now create the model which is called f
f = ifcopenshell.open(fn)

# a specific wall is defined here based on its GlobalID
# we are working with standard files so you should also be able to find this.
# the small diff is that this is working on the optimized version
wall = f["2O2Fr$t4X7Zf8NOew3FLPP"]

# This is the magic code that loads the geometry for the models into its own model - so that we can query the geometry (and in this case the 
tree_settings = ifcopenshell.geom.settings()
tree_settings.set(tree_settings.DISABLE_OPENING_SUBTRACTIONS, True)
t = ifcopenshell.geom.tree(f, tree_settings)

# you need the code below in both RWTH and if running it directly.
for space in model.by_type("IfcSpace"):
    near = space.BoundedBy
    print("\n\t####{}\n".format(space.Name))
    for objects in near:
        if (objects.RelatedBuildingElement != None):
            if (objects.RelatedBuildingElement.is_a('IfcDoor')):
                print(objects.RelatedBuildingElement.Name)
```

### Intermediate Example 3
Load file using tKinter

*This code is only a snippet*

```Python
# thanks to https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog

from Tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
```

### Intermediate Example 4a

Write data to excel.

1) type in the cmd line

<pre>pip install xlsxwriter</pre>

2) in your python file  type

```Python
import xlsxwriter # https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1

workbook = xlsxwriter.Workbook('output/future_format.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write(0,0, 'hello world')

workbook.close()
```

### Intermediate Example 4b

Write ifc data to excel files.

*This code include the import and model loading as it is a special case.*

```Python
# https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1

import ifcopenshell
import xlsxwriter 

# this line opens the workbook, if it doesn't exist it makes it, otherwise
# it will overwrite the existing file.
# if it dpes already exist please close it otherwise it will not work (it cannot read open files)
workbook = xlsxwriter.Workbook('output/future_format.xlsx')
# you have the workbook open, now specify the sheet you want to write to
worksheet = workbook.add_worksheet()
# this is extra code that you can include to format the cells in your document. You could shange this to other examples. to create other effects.
bold = workbook.add_format({'bold': True})

# this line loads the ifc model into python. - careful most internet examples use ifc_model, 
# but we are using model here, so that it also works in RWTH viewer.
# When RWTH viewer loads the model in the GUI it calls it model.
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")

# this is normally formatted
worksheet.write(0,0, 'hello')

# in this line we have added the bold argument defined previously with the add_format command to define the format of the cell.
worksheet.write(0,0, 'hello', bold)

# when you have finished editing the document it is essential to close the workbook.
# these saves the document.
workbook.close()
```

### Intermediate Example 4c

Write ifc data to excel files (in a function)

*This code include the import and model loading as it is a special case.*

```Python
import ifcopenshell
# we will use the xlswriter library below to work with excel in python.
import xlsxwriter # https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1
# make a folder called output and then this line will make an 
# excel in there if one doesn't exist already
# N.B. remember to close the workbook if you have it open 
# BEFORE you run this script!
workbook = xlsxwriter.Workbook('output/test.xlsx')
# open the model as normally
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")
# this is a function it enables you to repeat the same command
# and reduce the amount of code that you have :)
# the function is called makeASheet - you can call it anything...
# it has a brackets after it, this is where the argument goes...
def makeASheet(ifcType):
    sheet = workbook.add_worksheet(ifcType)
    # define which row you want to start writing at.
    row =1
    for entity in model.by_type(ifcType):
        # this writes the data to the sheet
        # sheet.write(row, column, data)
        sheet.write(row,0,str(entity.Name))
        # this 'iterates' row so that each time we step down a row.
        # otherwise each new entry would overwrite the previous entry.
        row+=1
# here we can call the function and put it the argument
# in this case we are asking for the results of 
# different IFC entities to be written to their own sheets       
makeASheet('IfcSlab')
makeASheet('IfcWall')
makeASheet('IfcCovering')
makeASheet('IfcBeam')
# it is important to close the workbook afterwards
workbook.close()
```

### Intermediate Example 5a

Read data from excel files

*This code include the import and model loading as it is a special case.*

```Python
import xlrd
import ifcopenshell

## open the workbook
workbook = xlrd.open_workbook('output/future_format.xlsx')
## print the number of sheets in the workbook
print (workbook.nsheets)
## print the name of the sheets in the workbook
print (workbook.sheet_names())
## open the sheets by index - open the first sheet of the workbook
first_sheet = workbook.sheet_by_index(0)
## print the values in the first row of the first sheet
print (first_sheet.row_values(0))
## print the values in the first row of the first sheet
print (first_sheet.col_values(0))
## read the first cell in the first sheet
cell = first_sheet.cell(0,0)
## print the first cell
print (cell)
## print the value contained in the first cell
print (cell.value)
```

### Intermediate Example 5b

Read data from excel file and IFC file

*This code include the import and model loading as it is a special case.*

```Python

import xlrd
import ifcopenshell

'''
For this example we take values from our assumptions sheet
based on the the global ids of the slabs in the model
'''

model = ifcopenshell.open("model/Duplex_A_20110907.ifc")

## Open the workbook
workbook = xlrd.open_workbook('output/future_format.xlsx')

## Open the assumptions sheet in the workbook
assumptions_sheet = workbook.sheet_by_index(4)

## loops though the stairs in the model
for slab in model.by_type('IfcSlab'):
    ## get the global id of the stair
    id = slab.GlobalId
    ## loops through the values in the first column of assumptionStair sheet
    for i in range(0, len(assumptions_sheet.col_values(0))):
        ##Get the cells in column A
        cell = assumptions_sheet.cell(i,0)
        ##Get the value of the cells
        value = cell.value
        ## Check if the value in the cell is the same as the global id of the slab
        if id == value:
            ## if the same id - print the value of the column B
            print(assumptions_sheet.cell(i,1).value)
```

### Intermediate Example 6

tKinter GUI

*This code is only a snippet*

```Python
# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()
```

[entities]: /Concepts/Entities
[use]: /Uses
[IDE]: /Concepts/IDE

## Glossary of terms (Work in progress)
- **F-string** - a "new", easier way of formatting print statements. It is more readable than the previous versions. Check out [this article](https://realpython.com/python-f-strings/) for more info.

	**Example**:
```Python
print(f"Some string {my_non_string_variable}")
```

- **Format** - an older way of formatting print statements -> check it out here [https://pyformat.info/](https://pyformat.info/)

	**Example**:

```Python
print("Some string {}".format(my_non_string_variable))
```

- **Input** - Get more information -> [https://www.w3schools.com/python/ref_func_input.asp
](https://www.w3schools.com/python/ref_func_input.asp
)
- **Function** - sometimes we might have to define a function for code that we will reuse in our script for instance [https://www.tutorialspoint.com/python/python_functions.htm](https://www.tutorialspoint.com/python/python_functions.htm)




