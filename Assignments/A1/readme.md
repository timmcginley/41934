# A1: Learning from OpenBIM (Forensic BIM)
Warm up project to get your teeth into OpenBIM standards. This assignment is linked to the following learning objectives.

*Aim: This assignment Focus on IFC analysis of real (previous) student building design projects from an [advanced building design course](https://github.com/timmcginley/41936) that runs in the previous semester.*
### Learning Objectives
2. Identify, locate and extract information from an IFC model in OpenBIM tools
3. Apply appropriate OpenBIM standards and guidelines to support open and FAIR data, tools and processes.
6. Create, fork, branch and collaborate on the development of an OpenBIM tool in Python with peers in a [code repository](/Concepts/Github/README.md).
7. Identify BIM challenges by analysing OpenBIM data.
   
 The Identify what the projects analysed, how did they test this? What was the domain focus of the investigation? Was it structural, energy and indoor, daylight, acoustic, LCA/LCC or something else? They should then be introduced to BPMN and use it to document the use case and explore the role of experts in OpenBIM. Following this, the students should review OpenBIM tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the problem identified in the design project in the previous part. Finally, they could check the information validity of the models against the use case requirements they identified. 


  The aim of this assignment is to become familiar with the core concepts of OpenBIM. This is done  through a deep dive into the IFC file format and associated Open BIM standards. The [IFC data model](/Concepts/IFC/README.md) is the industry standard for BIM, but many BIM practioners (and some BIM experts) still don't really understand it.

Previously we have focused on the IFC file and helping you to understand how it is structured, this year we will push this idea further by exploring the file in the awesome OpenBIM tool blender. This allows us the opportunity to pull several exercises together into the same environment.

## Assignment
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

### 03 A BPMN file
* Describes the use case
* Shows the exchange of information between the stakeholders in the use case
* Helps you to define the scope of your script
* Helps you to see what inputs and outputs your use case has.

## Submissions
### Cost
* [Group 01](https://github.com/kfjordt/11034-advanced-bim) - Cost (structural)
* [Group 02](https://github.com/AndersTraeland/A1---Open-BIM) - Cost (Structural)
* [Group 11](https://github.com/AnjaHolmquist/GROUP-11.) - Cost
* [Group 19](https://github.com/simonciversen/A1-OpenBIM) - Cost (early design phase)
### Structure
* [Group 09](https://github.com/katrinekolbjornsen/UsecaseA1) - Structural
* [Group 10](https://github.com/juliev1234/A1_OpenBim_Group10) - Structural
* Group 14 - no link - Structural
* Group 17 - no link - Structural
* [Group 20](https://github.com/Hajarb11/BIM--Group20) - Structural
* [Group 21](https://github.com/loicsan272/Advenced-BIM2022-G21) - Structural
### LCA
* [Group 03](https://github.com/WilliamEskildsen/41934_group3) - LCA
* [Group 04](https://github.com/MathildeDTU/41934-Advanced-BIM-F22) - LCA
* Group 16 - no link - LCA
### Energy / Indoor / Daylight / Acoustics
* [Group 06](https://github.com/gabrielamiti/BIM) - Indoor Energy and Daylight
* Group 15 - no link - Indoor climate analysis
* [Group 18](https://github.com/RikkeKHansen/Markdown-file) - Indoor climate
* [Group 22](https://github.com/s183578/41934-Advanced-BIM-Group-22) - Indoor Climate
* [Group 23](https://github.com/Enzuesta/41934-Advanced-BIM-Group23) - Daylight
* [Group 12](https://github.com/Jubelicool/A1-OpenBimGroup12) - Acoustics






