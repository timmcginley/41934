# A2: OpenBIM Modeller / Analyst

Focus on IFC analysis of real (previous) student building design projects from an advanced building design course that runs in the previous semester. Identify what the projects analysed, how did they test this? What was the domain focus of the investigation? Was it structural, energy and indoor, daylight, acoustic, LCA/LCC or something else? They should then be introduced to BPMN and use it to document the use case and explore the role of experts in OpenBIM. Following this, the students should review OpenBIM tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the problem identified in the design project in the previous part. Finally, they could check the information validity of the models against the use case requirements they identified.



You can choose between working in the assignment in
1. the modelling role or
2. the analysing role.

## A2A: OpenBIM Modelling
Aim: To learn from the experience of either modelling or analysing OpenBIM models collaboratively.

*Aim: This assignment Focus on IFC analysis of real (previous) student building design projects from an [advanced building design course](https://github.com/timmcginley/41936) that runs in the previous semester.*

### Learning Objectives
12. Evaluate [software licensing](/41934/Concepts/Software_licences) suitability and implications for the OpenBIM tool you develop or modelling tool you use.
    
### AIM:
The world of BIM modelling is also changing fast.

- Trad tools: I.e. Revit - please google it...
- Emerging OpenSourse Alternatives i.e. BlenderBIM [hEART]
- AI Augmented Modellers
the implicaitons  of AI augmented modelling are currently unknown - for an idea you could check out [Snaptrude](https://www.snaptrude.com/) although there are also lots of other tools.
Now includes Hypar and others.

This could include information and processes from other digital sources and platforms, i.e. 3D printing / rapid prototyping, as well as drone, mixed reality and laser scanning (Wang Liyuan et al., 2020). The main challenge here is to validate the BIM model and use current tools or tools of their own to fix issues efficiently. The model group would thoroughly check the received IFC file and fix missing or incorrect geometric and non-geometric information. This should be in collaboration with an analysis (A2B) group. Furthermore, they could develop their own models, but the emphasis in this assignment would be on maintaining, reusing and further developing existing models or sub systems (OpenBIM principle 2) for a specific disciplinary use case.

We introduce potential future BIM tools and then in class we investigate their connections and the roles they will play in your future careers. This assignment is linked to the following learning objectives.

## A2: Analyse

Identify what the projects analysed, how did they test this? What was the domain focus of the investigation? Was it structural, energy and indoor, daylight, acoustic, LCA/LCC or something else? They should then be introduced to BPMN and use it to document the use case and explore the role of experts in OpenBIM. Following this, the students should review OpenBIM tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the problem identified in the design project in the previous part. Finally, they could check the information validity of the models against the use case requirements they identified. 

### Learning Objectives:
6. Create, fork, branch and collaborate on the development of an OpenBIM tool in Python with peers in a [code repository](/41934/Concepts/Github).

### Aim: 
4. Provide professional disciplinary guidance based on OpenBIM analysis.
9. Identify and model a BIM use case based on the BIM challenges identified from analysis of an OpenBIM project in [BPMN](/41934/Concepts/BPMN/README.md).
10. Identify an appropriate [development methodology](/41934/Concepts/Development_methodology) for an OpenBIM tool or model to different use cases.
11. Apply and improve programming skills in Python to develop an OpenBIM tool or modelling skills in OpenBIM using your engineering domain expertise.
12. Evaluate [software licensing](/41934/Concepts/Software_licences/README.md) suitability and implications for the OpenBIM tool you develop or modelling tool you use.
   
This task would focus on analysing the models using scripts as in the previous years using BlenderBIM as an IDE (integrated development environment) incorporating a console, 3d view, IFC data model hierarchy, and IFC property views in one place. Additionally, this assignment would provide the opportunity for the student to develop their own OpenBIM tools in Python.

In this assignment we will develop a tool / workflow based on the use case you defined in the [previous assignment](/41934/Assignment/A3).<br>
The tool must:
* Address your [use case](/41934/Uses):

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

## Aim

We have gathered the four most exciting potential future (open)BIM technologies in this course however it is uncertain how they fit together and the design and engineering experience that they could provide you in your future careers.

Therefore, the aim of this assignment is in your groups to explore focused parts of this future (open) BIM ecosystem, supported by theory, frameworks and examples provided in the course lectures.

## Activity Completion

## ideas
* i would be really interested to see if we could change values in an SVG file and use this to edit and append the information in drawings.

[modelling]: /41934/Roles/Modeller
[analysing]: /41934/Roles/Analyst
