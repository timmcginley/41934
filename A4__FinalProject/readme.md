# A4: Final Project

In this assignment we will develop a tool / workflow based on the use case you defined in the [previous assignment](https://github.com/timmcginley/41934/tree/main/A3__UseCase).<br>
The tool must:
* Address your [use case](https://github.com/timmcginley/41934/tree/main/A3__UseCase):
* Ideally be written in Python, but can be other approaches in special cases if agreed with the course responsible.
* Be summarised in a 2 minute video.
You will produce one final tool in the following folders, the structure of which is summarised below.

## Tool / Workflow

The structure of this depends on the tool you have chosen to develop but it should:
1. be written in Python (mostly) so should contain a main.py file
2. if you hev used blender as the target for the tool, please also include a .blend file that we can load to check your project.
3. clearly seperated the code from the input data and resulting guidance (output) (if your output is a file).

The structure of this depends on the tool you have chosen but a base structure for your folder / github repository should be: 

````
  - FILE: readme.md // the most important file :) 
  + FOLDER *img* // folder to 
  + FOLDER *model*
    - FILE: duplex or something else (ifc)
  + FOLDER *input* (examples given below)
    - FILE: excel data for instance // could also be assumption data
    - FILE: material cost data in json format?
  + FOLDER: *output*
    - FILE: this is if the output for your tool is a file, for instance an excel file.
  - FILE: main.py // you may also have other python files in there, but make sure you start from main.py
  - other python files folders and code as required.
  
````

## 2 Minute Video
* Summary of the use case / why is this a challenge?
* Who is you tool for?
* Business and societal value
* Demo of the tool (if interaction / processing takes longer – edit the video 😊)
* details about the upload / submission of the videos will be given closer to the time.
