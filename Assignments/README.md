# Assignments

>As an advanced course in BIM our intention is not to ‘teach’ software but to introduce concepts and tools that enable you to answer your own questions. Ultimately the aim of the course is to suport you to learn through the collective development of a new ecosystem OpenBIM tools and techniques and teaching your future colleagues how to learn from OpenBIM too.
>Our hope for you in the course is that you gain the confidence to find the answers you are looking for in an open, instructor and peer supported environment.

1. [Forensic BIM](/Assignments/A1)
2. [Use Case](/Assignments/A2)
3. [Tool](/Assignments/A3)
4. [OpenBIM Champion](/Assignments/A4)
5. [Reflection](/Assignments/A5).


## A1	[Forensic BIM](A1)
* Exercises: Learn Blender / Bonsai and IfcOpenShell
* Tools: [Kaare](https://github.com/KaareH)'s awesome Bimscore tool
* Case: Validate claims made in Advanced Building Design Reports.

In the Advanced Building Design Course students submit Disciplinary specific BIM models in IFC along with Disciplinary 'subject reports' and a 'client report' which summarises the interdisciplinary design of a tall building.

[ cool picture to summarise the Advanced Buidlign Design Process ] 

You job in this assignment is to check a claim made made in either a team's subject or client report. Can what thye are saying be validated by the BIM.

To acheive this, you will first review the disciplinary IFC models in Blender with the Bonsai (fka BlenderBIM) plugin.

It is possible to get information and model properties in Blender, but this would be very slow, so we will then show you how to run a simple script in the Blender Python script window to automate this search.

Finally to submit 

This task would focus on analysing the models using scripts as in the previous years using Blender / Bonsai as an IDE (integrated development environment) incorporating a console, 3d view, IFC data model hierarchy, and IFC property views in one place.

Adapt and apply simple scripts to validate claims made in previous iterations of the [Advanced Building Design] course. In your [focus](/Focus/) groups you will check specfic claims made in their project reports. These could include: Project GFA, Spaces required in the project brief, facade transparency and many other examples. 

## A2	[Use Case](A2)
* Exercises: Use case modelling etc.
* Tools: BPMN.io and [MarkDown](/Concepts/Markdown)
* Case: Identify use case and propose tool to assess, provide feedback or support specific process in BIM project.

AIM: Analyze and improve real projects for a specific use case.
Focus on IFC analysis of real (previous) student building design projects from an advanced building design course that runs in the previous semester. Identify what the projects analysed, how did they test this? What was the domain focus of the investigation? Was it structural, energy and indoor, daylight, acoustic, LCA/LCC or something else? 

In this assignment, you will be introduced to [BPMN] and use it to document the use case and explore the role of experts in [OpenBIM]. Following this, you will review OpenBIM tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the challenge identified in the design project in this assignment.

## A3	[Tool](A3)
* Exercises: Review previous IfcOpenShell Tutorials [Basic] [Medium] and [Advanced]
* Tools: [Blender / Bonsai] | [Speckle] [Voxel toolkit]

This assignment provide the opportunity to develop your own OpenBIM tools in Python.

[ UPDATE THIS!!!!]

This task focuses on ISO 19650. The intention for autumn 2022 was to integrate real examples of 19650 into the course with practical examples, for instance by prototyping a total process using Speckle that complied to ISO 19650. However, time constraints in planning the course meant that this was ultimately replaced with traditional lectures from external parties. These provided informative content to the students but on their own were not enough for them to see the alignment to the other activities. A future BIM course should be focused on thinking in and gaining experience using ISO 19650 rather than just ‘teaching’ it. The experience of the autumn 2022 course enabled a proposal to map the development methodology (Figure 3) to ISO 19650 (Figure 4).


## A4	[Show & Tell](A4)
The final assignment focuses on the ability to transfer knowledge in an organization. It aims to address; how do we ‘learn from BIM’ at an organizational level? For this you will consider something you have learnt by yourselves that you think would be valuable to share with your peers. Suggested appraoches to support your peers learning could be, short tutorial videos, markdown files, carefully commented code and Jupyter notebooks. Furthermore, there is a chance to develop custom content that could be linked to the course learning environment that, with the student’s permission, could be used in future iterations of the course to support student learning, as well as in Advanced Building Design next year. Peer feedback will include how it supported them to make decisions and ultimately if it was clear enough to help them to know how to change their model.

## A5 [Reflection](A5)
A final brief report to offer you space to reflect on your learning compared to the course [learning goals]. This helps you to become more aware of what you learnt, what worked for you and how you can support both your own learning and that of your peers in the future.

[learning goals](/LearningObjectives/)

<!-- 2023

1. [Learning From OpenBIM](/Assignments/A1)
2. [OpenBIM Modeller / Analyst](/Assignments/A2)
3. [OpenBIM Manager / Ontologist](/Assignments/A3)
4. [OpenBIM Champion](/Assignments/A4)
5. [Reflection](/Assignments/A5).

## A1	[Learning from OpenBIM](A1)
IFC Dashboard project

## A2	[OpenBIM Modeler / Analysis](A2)
AIM: Analyze and improve real projects for a specific use case.
Focus on IFC analysis of real (previous) student building design projects from an advanced building design course that runs in the previous semester. Identify what the projects analysed, how did they test this? What was the domain focus of the investigation? Was it structural, energy and indoor, daylight, acoustic, LCA/LCC or something else? They should then be introduced to BPMN and use it to document the use case and explore the role of experts in OpenBIM. Following this, the students should review OpenBIM tools made in the previous year of the OpenBIM course and identify which tools could be used or adapted to solve the problem identified in the design project in the previous part. Finally, they could check the information validity of the models against the use case requirements they identified.
### Modeler
This could include information and processes from other digital sources and platforms, i.e. 3D printing / rapid prototyping, as well as drone, mixed reality and laser scanning (Wang Liyuan et al., 2020). The main challenge here is to validate the BIM model and use current tools or tools of their own to fix issues efficiently. The model group would thoroughly check the received IFC file and fix missing or incorrect geometric and non-geometric information. This should be in collaboration with an analysis (A2B) group. Furthermore, they could develop their own models, but the emphasis in this assignment would be on maintaining, reusing and further developing existing models or sub systems (OpenBIM principle 2) for a specific disciplinary use case.
### Analyst
This task would focus on analysing the models using scripts as in the previous years using BlenderBIM as an IDE (integrated development environment) incorporating a console, 3d view, IFC data model hierarchy, and IFC property views in one place. Additionally, this assignment would provide the opportunity for the student to develop their own OpenBIM tools in Python.

## A3	[OpenBIM Manager / Ontologist](A3)
### Manager
This task focuses on ISO 19650. The intention for autumn 2022 was to integrate real examples of 19650 into the course with practical examples, for instance by prototyping a total process using Speckle that complied to ISO 19650. However, time constraints in planning the course meant that this was ultimately replaced with traditional lectures from external parties. These provided informative content to the students but on their own were not enough for them to see the alignment to the other activities. A future BIM course should be focused on thinking in and gaining experience using ISO 19650 rather than just ‘teaching’ it. The experience of the autumn 2022 course enabled a proposal to map the development methodology (Figure 3) to ISO 19650 (Figure 4).
### Ontologist
The focus of this assignment is to support the Ontologist role. This should cover both Open Linked building data and traditional classification systems.

## A4	[OpenBIM Champion](A4)
The final assignment focuses on the ability to transfer knowledge in an organization. It aims to address; how do we ‘learn from BIM’ at an organizational level? This is a new component for autumn 2023. For autumn 2023, participants will therefore have to consider how to teach what they have learnt in the process to another group of students. Ideally this would support those that choose Analysis in the 2nd assignment to learn about modelling, or for the ontologists to learn about management. Suggested tools include, short tutorial videos, markdown files, carefully commented code and Jupyter notebooks. Furthermore, there would be a chance for them to develop custom content that could be linked to in the course learning environment that, with the student’s permission, could be used in future iterations of the course to support student learning.

## A5 [Reflection](A5)

A2 and A3 have 2 options, so participants will help to evaluate and provide peer feedback on each other’s work. 

Participants will get an introductory lecture (video) to both options to support their choice (Adamu & Thorpe, 2016). In this way, the modelling groups will receive guidance from the analysis groups and provide feedback on that guidance back to them. This feedback should also include how it supported them to make decisions and ultimately if it was clear enough to help them to know how to change their model.

-->
