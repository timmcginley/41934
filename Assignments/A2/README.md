# A2: Analysis

*Aim: This assignment Focus on IFC analysis of real (previous) student building design projects from an [advanced building design course](https://github.com/timmcginley/41936) that runs in the previous semester.*

Focus on IFC analysis of real (previous) student building design projects from an advanced building design course that runs in the previous semester. 

In this activity you will be introduced to a [‘metadisciplinary framework’ for BIM (McGinley Krijnen, 2022)](https://www.researchgate.net/publication/363579368_A_framework_for_meta-disciplinary_building_analysis/stats). 

## A2A: Install Blender and the BlenderBIM plugin.
Previously we have focused on the IFC file and helping you to understand how it is structured, this year we will push this idea further by exploring the file in the awesome OpenBIM tool [Blender] and its openBIM plugin [BlenderBIM]. This allows us the opportunity to pull several exercises together into the same environment.

## A2B: Convert Old Advanced Building Design Models
* Select one of the provided models.
* Translate the models to [IFC4] following the Dikon method.
* Read the project reports.
![image](https://github.com/timmcginley/41934/assets/1415855/741ab321-fe1c-43a6-ae79-057d4ee9e6e9)

## A2C: Import the IFC into BlenderBIM
* Import one of the 41936 models into [BlenderBIM] and explore the IFC file and its properties.

## A2D: Explore the script
* In the scripting window you can then use IfcOpenShell to further explore the model (we provide examples)
* You will identify a simple BIM Use case examples could be gathering:
* areas of the building,
* quantities of materials,
* could you estimate cost? - if so how?

## A2E: Check the numbers
Identify what the projects analysed, how did they test this? What was the domain focus of the investigation? Was it structural, energy and indoor, daylight, acoustic, LCA/LCC or something else? They should then be introduced to BPMN and use it to document the use case and explore the role of experts in OpenBIM. Following this, the students should review OpenBIM tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the problem identified in the design project in the previous part. Finally, they could check the information validity of the models against the use case requirements they identified. 
* develop scripts to help teams in future analyse their buildings.
  
Identify what the projects analysed, how did they test this? What was the domain [focus] of the investigation? Was it [structural], [energy and indoor, daylight, acoustic], [LCA/LCC], [construction planning] or something else? You will then be introduced to [BPMN] and use it to document the use case and explore the role of experts in [OpenBIM]. 
* Which  [focus area](s) will you choose?
* What information did you find that helped you to see this would be a good choice?

## A2F: Review previous code
Following this, you will review [OpenBIM] tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the problem identified in the design project in the previous part. Finally, they could check the information validity of the models against the use case requirements they identified.

This task would focus on analysing the models using scripts as in the previous years using BlenderBIM as an IDE (integrated development environment) incorporating a console, 3d view, IFC data model hierarchy, and IFC property views in one place. Additionally, this assignment would provide the opportunity for the student to develop their own OpenBIM tools in Python.

## A2G: Analyze project Reports
* Now review the project reports - can you check that the values they say they acheived are actually acheived?

## A2H: Develop your own script

* Develop a script in [IfcOpenShell] (based on examples and support from the teachers) to check a specific claim one of the reports relevant to your [focus] area.

## A2I: Produce a Guide
* Report – is it accurate?
* What are the problems with
* The BIM
* The Building
* The Process
* The Engineering

## Activity Completion
Your group must submit your modified script file for the use case, this should be provided in a ‘repo’ in the github account linked to your group. The repo will include:

### 01 Python script
* Your main.py file that is a copy of the script we can run in Blender.

### 02 A markdown file that describes: 
* Describe the use case you have chosen
* Who is the use case for?	
* What disciplinary (non BIM) expertise did you use to solve the use case
* What IFC concepts did you use in your script (would you use in your script)
* What disciplinary analysis does it require?	
* What building elements are you interested in?	
* What (use cases) need to be done before you can start your use case?	
* What is the input data for your use case?	
* What other use cases are waiting for your use case to complete?

### 03 A BPMN file
* Describes the use case
* Shows the exchange of information between the stakeholders in the use case
* Helps you to define the scope of your script
* Helps you to see what inputs and outputs your use case has.

### Learning Objectives

4. Provide professional disciplinary guidance based on OpenBIM analysis.
6. Create, fork, branch and collaborate on the development of an OpenBIM tool in Python with peers in a [code repository](/41934/Concepts/Github).
9. Identify and model a BIM use case based on the BIM challenges identified from analysis of an OpenBIM project in [BPMN](/41934/Concepts/BPMN/README.md).
10. Identify an appropriate [development methodology](/41934/Concepts/Development_methodology) for an OpenBIM tool or model to different use cases.
11. Apply and improve programming skills in Python to develop an OpenBIM tool or modelling skills in OpenBIM using your engineering domain expertise.
12. Evaluate [software licensing](/41934/Concepts/Software_licences/README.md) suitability and implications for the OpenBIM tool you develop or modelling tool you use.
    

## ANALYSIS TOOL SPECIFICATION

In this assignment we will develop a tool / workflow based on the use case you defined in the [previous assignment](/41934/Assignment/A3).<br>
The tool must:
* Address your [use case] :

* Ideally be written in Python, but can be other approaches in special cases if agreed with the course responsible.
* Be summarised in a 2 minute video.
You will produce one final tool in the following folders, the structure of which is summarised below.

## Tool / Workflow

The structure of this depends on the tool you have chosen to develop but it should:
1. be written in Python (mostly) so should contain a main.py file
2. if you have used blender as the target for the tool, please also include a .blend file that we can load to check your project.
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
* Summary of the [use case] / why is this a challenge?
* Who is your tool for?
* Specify the [Business and societal value] of your analysis tool / process.
* Demo of the tool (if interaction / processing takes longer – edit the video 😊)
* details about the upload / submission of the videos will be given closer to the time.

## Aim

We have gathered the four most exciting potential future (open)BIM technologies in this course however it is uncertain how they fit together and the design and engineering experience that they could provide you in your future careers.

Therefore, the aim of this assignment is in your groups to explore focused parts of this future (open) BIM ecosystem, supported by theory, frameworks and examples provided in the course lectures.

## Activity Completion

## Ideas
* How could we change values in an SVG file and use this to edit and append the information in drawings.
* Hwo could future students in [Advanced Building Design] use your tool

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
