# A1: Forensic BIM
Exercises: Learn Blender / Bonsai and IfcOpenShell
Tools: Kaare's awesome Bimscore tool
Case: Validate claims made in Advanced Building Design Reports.

**The aim of this assignment is to become familiar with the core concepts of OpenBIM**. This is done through a deep dive into the IFC file format and associated Open BIM standards. The [IFC data model](/Concepts/IFC) is the industry standard for BIM, but many BIM practioners (and some BIM experts) still don't really understand it.

## Task
Apply simple scripts to validate claims made in previous iteraitons of the [Advanced Building Design] course. In your [focus] groups you will check specfic claims made in their project reports. aS example these could (depending on your focus area) include: 
* Project GFA,
* Spaces required in the [project brief](/41936/Project/Breif)
* Energy Frame
* Facade transparency ...
* What other things can you think of?

You will analyse the models using scripts as in the previous years using Blender / Bonsai as an IDE (integrated development environment) incorporating a console, 3d view, IFC data model hierarchy, and IFC property views in one place.


## Steps

### 1) Make a group 
* 2 people - exceptionally could be 3
### 2) Choose a [focus] area / subject.
* Find a focus area / subject that you are interested in - the point of the focus area is to help your group have a common aim.
* You 

### 3) Review Project documentation for that focus area.
* It is important to look at all 4 projects. Both for the subject report you have selected and client report.
* Have a look at the BEATS and see how these are used in the project.
* For each subject we require one manager group. The job of this group will be to coordinate the different groups in the subject area.
* The manager will support the [analysts] by coordinating their work.


### 3) Select a claim to check.
* it could be one of the BEATS.
* It could be a number from the poster for the year.
* It does not need to be a super complicated number.

* Inside your focus area, find a claim that the team has made from one of the projects we have given you.
* find a use case or a "problem" you'd want to solve. If your focus area was "indoor climate", an example of a use case could be "calculate Daylight Autonomy for every space".
  
### 4) Install Blender / Bonsai
* Follow the instructions [here] to install [Blender] and [Bonsai]

### 5) Have a look around

* You can use this [tool from Dion Moult](https://blenderbim.org/search-ifc-class.html) to help find the entities you are looks for also you can [search the IFC4 schema here](https://ifc43-docs.standards.buildingsmart.org/)
     
### 6) Run the [Bimscore] tool
* add a custom function
* coordinate your function with your subject BIM manager to make it run in the stack and generate the HTML report for your subject.

### 7) submit your report / update your github diary.

This assignment supports the following [learning objectives].

### Learning Objectives
2. Identify, locate and extract information from an [IFC] model in [OpenBIM] tools
3. Apply appropriate [OpenBIM standards] and guidelines to support open and [FAIR] data, tools and processes.
7. Identify [BIM] challenges by analysing [OpenBIM] data.

## Submission 2024
Enrolled students submit on DTU Learn [here](https://learn.inside.dtu.dk/d2l/lms/dropbox/user/folders_list.d2l?ou=215344&isprv=0)

<!-- links --> 

[learning objectives]: /41934/LearningObjectives
[Blender]: /41934/Concepts/Blender
[Bonsai]: /41934/Concepts/Bonsai
[OpenBIM standards]: /41934/Concepts/Standards
[BIM]: /41934/Concepts/BIM
[OpenBIM]: /41934/Concepts/OpenBIM
[FAIR]: /41934/Concepts/FAIR
[focus]: /41934/Focus
[Advanced Building Design]: /41946/

<!--
### 3) Choose the relevant model from the Stanford / Skylab models
* Download the [Stanford models](https://learn.inside.dtu.dk/d2l/le/content/167582/Home) or Skylab models (on Learn -> "IFC Models" -> "Stanford models" - *Enrolled Students Only*
* Select the model that best represents your focus area.

### 4) Convert the IFC to an Excel work book using the IFA tool
[IFA Tool](/41934/Concepts/IFCFileAnalyzer)

* Install IFA
* generate the spreadsheet

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

-->
