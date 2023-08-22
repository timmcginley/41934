# A1: Learning from OpenBIM (Forensic BIM)
Warm up project to get your teeth into OpenBIM standards. This assignment is linked to the following learning objectives.

### Learning Objectives
2. Identify, locate and extract information from an IFC model in OpenBIM tools
3. Apply appropriate OpenBIM standards and guidelines to support open and FAIR data, tools and processes.
7. Identify BIM challenges by analysing OpenBIM data.

Identify what the projects analysed, how did they test this? What was the domain focus of the investigation? Was it structural, energy and indoor, daylight, acoustic, LCA/LCC or something else? They should then be introduced to BPMN and use it to document the use case and explore the role of experts in OpenBIM. Following this, the students should review OpenBIM tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the problem identified in the design project in the previous part. Finally, they could check the information validity of the models against the use case requirements they identified. 

**The aim of this assignment is to become familiar with the core concepts of OpenBIM**. This is done through a deep dive into the IFC file format and associated Open BIM standards. The [IFC data model](/Concepts/IFC/README.md) is the industry standard for BIM, but many BIM practioners (and some BIM experts) still don't really understand it.

Previously we have focused on the IFC file and helping you to understand how it is structured, this year we will push this idea further by exploring the file in the awesome OpenBIM tool blender. This allows us the opportunity to pull several exercises together into the same environment.

In this activity you will be introduced to a [‘metadisciplinary framework’ for BIM (McGinley Krijnen, 2022)](https://www.researchgate.net/publication/363579368_A_framework_for_meta-disciplinary_building_analysis/stats). 

## Assignment

2 options:
1. BlenderBIM
2. [IFC Analyser](Concepts/IFCFileAnalyzer)

Building Options
1. Advanced Building Design
2. Skylab

## BlenderBIM
Install Blender and the BlenderBIM plugin.
Import one of the course example files into Blender and explore the IFC file and its properties.
In the scripting window you can then use IfcOpenShell to further explore the model (we provide examples)
You will identify a simple BIM Use case examples could be gathering:
areas of the building,
quantities of materials,
could you estimate cost? - if so how?

Now review the project reports - can you check that the values they say they acheived are actually acheived?

Develop a script (based on examples and support from the teachers) to check a specific calim in one of the reports.

## Activity Completion
Your group must submit your modified script file for the use case, this should be provided in a ‘repo’ in the github account linked to your group. The repo will include:

### 01 Python script
* Your main.py file that is a copy of the script we can run in Blender.
* *THIS CAN BE WORK IN PROGRESS* 

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

### Select a focus Area
* Which of the [focus areas](/41934/Focus) will you choose?
* What information did you find that helped you to see this would be a good choice?
* In the next assignment will you focus on modelling or analysis?

### 03 A BPMN file
* Describes the use case
* Shows the exchange of information between the stakeholders in the use case
* Helps you to define the scope of your script
* Helps you to see what inputs and outputs your use case has.





