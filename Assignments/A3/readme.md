# A3 OpenBIM Manage / Ontology

## A3A: Manage
Aim: 
Learning Objectives
1. Create and manage a BIM Execution Plan based on the OpenBIM standard [ISO 19650](/Concepts/ISO19650/README.md)
7. Identify and model a BIM use case based on the BIM challenges identified from analysis of an OpenBIM project in BPMN.
   
This task focuses on ISO 19650. The intention for autumn 2022 was to integrate real examples of 19650 into the course with practical examples, for instance by prototyping a total process using Speckle that complied to ISO 19650. However, time constraints in planning the course meant that this was ultimately replaced with traditional lectures from external parties. These provided informative content to the students but on their own were not enough for them to see the alignment to the other activities. A future BIM course should be focused on thinking in and gaining experience using ISO 19650 rather than just ‘teaching’ it. The experience of the autumn 2022 course enabled a proposal to map the development methodology (Figure 3) to ISO 19650 (Figure 4).


### Overview
We want you to think of BIM as a method for you to get information and perform analysis on models for things that interest you. Therefore, in this assignment we want you to work on a use case that you are really passionate about and want to explore further which you can develop further in your final project. For this activity you need to further develop and analyse your BIM Use Case. Advanced BIM isn’t about changing everything at once. It is about focusing on a specific use case, and starting to think about how you would test a potential solution to that use case before you build the solutions. It is about considering, the information that you need - what can you get from the IFC for instance? In this activity you will
* Identify the IFC entities and properties you will need for your use case.
* describe the existing process in a BPMN (this time you can be more specific.
 * describe the proposed process in a BPMN (this time you can be more specific).
You should use this activity to clearly scope your ambition and motivation for your OpenBIM workflow / tool. The idea is to reduce the potential to overstretch and provide an opportunity to demonstrate the potential (business) value that your tool could offer.

### Content
In this assignment you will dig deeper into use cases and some tools and standards to support this and develop two BIM use case that extends provide a real example of a BIM use that you can then use to develop your final project (you will choose one of these BIM uses for the final project).

### Assignment Format
Therefore, the core of the assignment is to produce a readme.md in markdown for your selected use case. For more information about markdown, please check out this awesome markdown tutorial.
Assignment should include
Report (documenting sections 1-10)
Readme.md
Information exchange excel sheet (for section 4)
Use_case_INFX_Team_XX.xlsx
Should include:
1.	BPMN file of current use case (redrawn by you) + 
2.	BPMN file for your proposed tool. 
If you download this from bpmn.io as an svg you should be able to place this in an img folder in your github repo and then show it in the readme file.
```
![Alt text](name of SVG file)
<img src=" img/name_of_svg_file.svg ">
```

## The report
You should produce a report written in markdown. The contents of the report are based on a hybrid of full Information delivery manuals, the BIM Execution Plan from Penn State and common development methodologies from computer science. in this sense, the use case report you will produce for this assignment is special as it includes the plan for the development of a new tool / workflow. It should include the following parts

### 3A: Analyse use case
1. Goal: Goal of the tool / workflow in one sentence. i.e. to support the user to calculate the total total cost of the project.
2.  Model Use (Bim Uses): Please refer initially to the Mapping BIM uses, use cases and processes section in this document.

### 3B: Propose a (design for a) tool / workflow
3. Process: model the process diagram from your use case in BPMN.io please remember to save the .bpmn file and you can save a .svg file that you can insert into your report. 
4. description of the process of your tool / workflow.

### 3C: Information exchange
5. Information Exchange: Fill out the excel template with the information for your planned tool / workflow. For this you will need access to the excel, and the Dikon document to help you specify the LOD (LOR,LOG,LOI) for each element you need for you tool / workflow. This can get confusing - don’t worry we can help 😊
6. IFC: Describe the IFC entities and properties for each of the elements you identified in your information exchange. Describe the data that you need to:
	* Find in the IFC
	* Find in an external sources i.e. BR18
	* Based on assumptions (useful when we don't have the 'real' data that we need for our tool)

### 3D: Value What is the potential improvement offered by this tool?
This is the common question when developing tools and processes as an [intrapreneur]( https://hbr.org/2020/03/why-you-should-become-an-intrapreneur) in a company. You should consider the business and societal value of this tool – does it save time to the company, does it make employees happier / more productive? Could it reduce material use in society?

7.	Describe the business value (How does it create value for your business / employer)
8.	Describe the societal value (How does it make the world better)

* N.B. If it doesn't do either of these things (ideally it should do both - don't do it!!)

### 3E: Delivery
In this assignment we will focus on the input data that you need for your final tool / workflow. 
9. Your tool/workflow: Description of how your tool / workflow would solve the use case
10. Delivery: Description of how you would make the tool / workflow - what steps would you go through?
