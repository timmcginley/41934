# A2: Analysis

## A2A: Import the IFC model into BlenderBIM
* Import one of the Skylab models into [BlenderBIM] and explore the IFC file and its properties.

## A2B: Explore the script
* In the scripting window you can then use IfcOpenShell to further explore the model by following examples in the [tutorials](/41934/Examples/IfcOpenShell/Basic).

## A2C: Identify a BIM use case.
Examples of use cases could be:
* Calculate structural integrity of beams and columns.
* Perform an LCA of the building.
* Perform a daylight analysis of all the relevant spaces.

## A2D: Create a BPMN diagram of the use case
You can use this online tool to create a [BPMN file](https://bpmn.io/).
A diagram should:
* Describe all stages and processes of the use case
* Show the inputs and outputs between your tool and other data models, experts, stakeholders etc.
* Clearly show the exchange of information between your tool and the IFC model. Which specific classes are being checked or manipulated?

See [this document](https://standards.buildingsmart.org/documents/IDM/IDM_guide-QuickGuideToBPMN-2007_01.pdf) from buildingSMART for more information about creating [IDM](/41934/Concepts/IDM) diagrams using BPMN.

## A2E: Define the scope of your script
Using the diagram of your use case, identify the a part of it that you can execute in your script.
You can either clearly mark the part of the diagram from A2D that defines your scope or you can produce a new diagram.
Show the processes and logic of your tool in as much detail as possible (whithin reason). What information are you extracting and what happens with it throughout the script?

Focus on the early stage the larger use case, that is checking the model for information and either getting it ready for further simulations or maybe doing some simple calculations.


## A2F: Develop your own script

Now you can begin to develop an [IfcOpenShell] script that follows your script diagram from A2E.

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

### 03 A markdown file that describes: 
* Describe the use case you have chosen.
* Who is the use case for?	
* What disciplinary (non BIM) expertise did you use to solve the use case?
* What IFC concepts did you use in your script (or would you use in the rest of the tool)?
* What disciplinary analysis does it require?	
* What building elements are you interested in?	
* What (use cases) need to be done before you can start your use case?	
* What is the input data for your use case?	
* What other use cases are waiting for your use case to complete?

### 04 A BPMN diagram saved as SVG or PNG.
* Describes the use case
* Shows the exchange of information between the stakeholders in the use case
* Helps you to see what inputs and outputs your use case has.

### 04.5 A modified BPMN diagram saved as SVG or PNG that defines the scope of your tool.
* Helps you to define the scope of your script


### Learning Objectives

4. Provide professional disciplinary guidance based on OpenBIM analysis.
6. Create, fork, branch and collaborate on the development of an OpenBIM tool in Python with peers in a [code repository](/41934/Concepts/Github).
9. Identify and model a BIM use case based on the BIM challenges identified from analysis of an OpenBIM project in [BPMN](/41934/Concepts/BPMN/README.md).
10. Identify an appropriate [development methodology](/41934/Concepts/Development_methodology) for an OpenBIM tool or model to different use cases.
11. Apply and improve programming skills in Python to develop an OpenBIM tool or modelling skills in OpenBIM using your engineering domain expertise.
12. Evaluate [software licensing](/41934/Concepts/Software_licences/README.md) suitability and implications for the OpenBIM tool you develop or modelling tool you use.
    


<!-- links --> 

[learning objectives]: /41934/LearningObjectives
[Blender]: /41934/Concepts/Blender
[OpenBIM standards]: /41934/Concepts/Standards
[BIM]: /41934/Concepts/BIM
[FAIR]: /41934/Concepts/FAIR
[focus area]: /41934/Focus
[IfcOpenShell]: /41934/Concepts/IfcOpenShell
[IFC4]: /41934/Concepts/IFC
[modelling]: /41934/Roles/Modeller
[analysing]: /41934/Roles/Analyst
[focus]: /41934/Focus
[OpenBIM]: /41934/OpenBIM
[BPMN]: /41934/Concepts/BPMN
[structural]: /41934/Focus/Structural
[energy and indoor, daylight, acoustic]: /41934/Focus/Indoor
[LCA/LCC]: /41934/Focus/Sustainability
[construction planning]: /41934/Focus/Build
[BlenderBIM]: /41934/Concepts/BlenderBIM
[use case]: /41934/Uses
[Business and societal value]: /Concepts/BusinessAndSocietalValue
[Advanced Building Design]: https://github.com/timmcginley/41936/tree/main
