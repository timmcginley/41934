# A1: Forensic BIM
Exercises: Learn Blender / Bonsai and IfcOpenShell
Tools: Kaare's awesome Bimscore tool
Case: Validate claims made in Advanced Building Design Reports.

**The aim of this assignment is to become familiar with the core concepts of OpenBIM**. This is done through a deep dive into the IFC file format and associated Open BIM standards. The [IFC data model](/Concepts/IFC) is the industry standard for BIM, but many BIM practioners (and some BIM experts) still don't really understand it.

## Task
Apply simple scripts to validate claims made in previous iteraitons of the [Advanced Building Design] course. In your focus groups you will check specfic claims made in their project reports. These could include: Project GFA, Spaces required in the project brief, facade transparency and many other examples.

You will analyse the models using scripts as in the previous years using Blender / Bonsai as an IDE (integrated development environment) incorporating a console, 3d view, IFC data model hierarchy, and IFC property views in one place.


## Steps

### 1) Make a group 
* 2 people - exceptionally could be 3
### 2) Choose a [focus area].
* Find a focus area that you are interested in - it could be two that overlap if you cannot decide on one, the point of the focus area is to help your group have a common aim and also to make it easier to manage the tools you create.

### 3) Review Project documentation for that focus area - 

### 3) Select a claim to check.

* Inside your focus area, find a claim that the team has made from one of the projects we have given you.
* find a use case or a "problem" you'd want to solve. If your focus area was "indoor climate", an example of a use case could be "calculate Daylight Autonomy for every space".
  
### 3) Choose the relevant model form the Stanford / Skylab models
* Download the [Stanford models](https://learn.inside.dtu.dk/d2l/le/content/167582/Home) or Skylab models (on Learn -> "IFC Models" -> "Stanford models" - *Enrolled Students Only*
* Select the model that best represents your focus area.

### 4) Convert the IFC to an Excel work book using the IFA tool
[IFA Tool](/41934/Concepts/IFCFileAnalyzer)

* Install IFA
* generate the spreadsheet

### 5) Have a look around

* You can use this [tool from Dion Moult](https://blenderbim.org/search-ifc-class.html) to help find the entities you are looks for also you can [search the IFC4 schema here](https://ifc43-docs.standards.buildingsmart.org/)
     
### 6) Add a sheet to the work book you have generated, then use data from the other sheets to provide a dashboard of the building.

What you choose to represent in your dashboard is up to you, but it should match the focus area and use case you have chosen. Think about what information would be necessary to solve your use case.

You could consider trying to represent:

* areas of the building,

* quantities of materials,

* could you estimate cost? - if so how?

* what else can you find in the IFC data that you could use in your dashboard?

### 6.a) Add a sentence about your use case at the top of your dashboard. Concider how the information you're showing supports your use case.

### 7) Submission

Your group must submit your modified excel including the dashboard sheet as the first sheet in the workbook.

You are not submitting any reports with this, so make sure that your dashboard is easy to understand - how do we know what we are looking at, and what you tried to do?

This assignment supports the following [learning objectives].

### Learning Objectives
2. Identify, locate and extract information from an [IFC] model in [OpenBIM] tools
3. Apply appropriate [OpenBIM standards] and guidelines to support open and [FAIR] data, tools and processes.
7. Identify [BIM] challenges by analysing [OpenBIM] data.


<!-- links --> 

[learning objectives]: /41934/LearningObjectives
[Blender]: /41934/Concepts/Blender
[BlenderBIM]: /41934/Concepts/BlenderBIM
[OpenBIM standards]: /41934/Concepts/Standards
[BIM]: /41934/Concepts/BIM
[OpenBIM]: /41934/Concepts/OpenBIM
[FAIR]: /41934/Concepts/FAIR
[focus area]: /41934/Focus
