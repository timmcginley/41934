# A4: Custom Tool

In this assignment we will develop a tool / workflow based on the use case you defined in the [previous assignment](https://github.com/timmcginley/41934/tree/main/A3__UseCase):
The tool must:
* Address your [use case](https://github.com/timmcginley/41934/tree/main/A3__UseCase):
* Ideally be written in Python, but can be other approaches in special cases if agreed with the course responsible.
* Be summarised in a 2 minute video.
You will produce one final tool in the following folders, the structure of which is summarised below.
## 1. Input
This includes any data that you are using in your tool this must also include you may also include any assumption data that you are pulling into your script.

## 2. Your tool
The tool should develop one of the use case you identified in A3.

## Submission structure 

This assumes that you are doing a normal python project.

Contents of your folder / github repository
````
  - FILE: readme.md // the most important file :) 
  + FOLDER: img // folder to 
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


## 1. Python script to produce Excel based on IFC
1. a python script to gather the data that you need for your project. This python script should produce an excel file containing the data from the IFC that you need in your project. for this we want you to:
* be careful about the naming of the sheets as this provides the hierarchy of information that you want to use in your tool.
## 2. Excel including assumptions and external data
* Some data may not be available in the model. In this case produce a second excel file that contains the assumptions for the use case...
## 2 minute video
* Summary of the use case / why is this a challenge?
* Who is you tool for?
* Business and societal value
* Demo of the tool (if interaction / processing takes longer – edit the video 😊)
* details about the upload / submission of the videos will be given closer to the time.
