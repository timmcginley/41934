# A3 OpenBIM Change

## A3A Reduce
* Produce a [BIM execution plan] (BEP) for the assignment

## A3B Reflect
* Check the new numbers – using your scripts from the previous assignment
* Check your conformance to the BEP.

## A3B Remodel
** Usecase: the Skylab-model (it is allowed to use other models, but they need to be IFC4 formatted)
Purpose: *modify, add* or *subtract* information in the model by using IfcOpenShell (You decide what modification is needed)


### Learning Objectives
1. Create and manage a [BIM Execution Plan based](/41934/Concepts/BIMEexecutionPlan) on the OpenBIM standard [ISO 19650](/41934/Concepts/ISO19650/README.md)
7. Identify and model a BIM use case based on the BIM challenges identified from analysis of an OpenBIM project in BPMN.
   
This task focuses on ISO 19650. The intention for autumn 2022 was to integrate real examples of 19650 into the course with practical examples, for instance by prototyping a total process using Speckle that complied to ISO 19650. However, time constraints in planning the course meant that this was ultimately replaced with traditional lectures from external parties (Molio). These provided informative content to the students but on their own were not enough for them to see the alignment to the other activities. A future BIM course should be focused on thinking in and gaining experience using ISO 19650 rather than just ‘teaching’ it. The experience of the autumn 2022 course enabled a proposal to map the development methodology (Figure 3) to ISO 19650 (Figure 4).

The structure of this depends on the tool you have chosen to develop but it should:
1. be written in Python (mostly) so should contain a main.py file
2. if you have used blender as the target for the tool, please also include a .blend file that we can load to check your project.
3. have clearly seperated the code from the input data and resulting guidance (output) (if your output is a file).

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

> [Removed from delivery in this assignment] ## 2 Minute Video
 
> * Summary of the use case / why is this a challenge?
> * Who is you tool for?
> * Business and societal value
> * Demo of the tool (if interaction / processing takes longer – edit the video 😊)
> * details about the upload / submission of the videos will be given closer to the time.


## A3B: Ontology
### Learning Objectives
5. Apply domain specific linked data ontologies.
11. Apply and improve programming skills in Python to develop an OpenBIM tool or modelling skills in OpenBIM using your engineering domain expertise.
   
The focus of this assignment is to support the Ontologist role. This should cover both Open Linked building data and traditional classification systems.

### Overview
We want you to think of BIM as a method for you to get information and perform analysis on models for things that interest you. Therefore, in this assignment we want you to work on a use case that you are really passionate about and want to explore further which you can develop further in your final project. For this activity you need to further develop and analyse your BIM Use Case. Advanced BIM isn’t about changing everything at once. It is about focusing on a specific use case, and starting to think about how you would test a potential solution to that use case before you build the solutions. It is about considering, the information that you need - what can you get from the IFC for instance? In this activity you will
* Identify the IFC entities and properties you will need for your use case.
* describe the existing process in a BPMN (this time you can be more specific).
You should use this activity to clearly scope your ambition and motivation for your OpenBIM workflow / tool. The idea is to reduce the potential to overstretch and provide an opportunity to demonstrate the potential (business) value that your tool could offer.

### Content
In this assignment you will dig deeper into use cases and some tools and standards to support this and develop two BIM use case that extends provide a real example of a BIM use that you can then use to develop your final project (you will choose one of these BIM uses for the final project).

### Assignment Format
Therefore, the core of the assignment is to produce a readme.md in markdown for your selected use case. For more information about markdown, please check out this awesome markdown tutorial.
Assignment should include
Report (documenting sections 1-10)
Readme.md
Information exchange excel sheet (for section 4): Use_case_INFX_Team_XX.xlsx
IDM diagrams:
1.	BPMN file of current use case (as implemented by you) + 
2.	BPMN file of the use case with additional/modified improved functions (which you would like to see implemented) 
If you download this from bpmn.io as an svg you should be able to place this in an img folder in your github repo and then show it in the readme file.
It may be beneficial to divide up or make multiple focused diagrams (BPMN files) showing an *Overview, Portions* or *Details* of the execution plan.

```
![Alt text](name of SVG file)
<img src=" img/name_of_svg_file.svg ">
```

## The report
You should produce a report written in markdown. The contents of the report are based on a hybrid of full Information delivery manuals, the BIM Execution Plan from Penn State and common development methodologies from computer science. in this sense, the use case report you will produce for this assignment is special as it includes the plan for the development of a new tool / workflow. It should include the following parts

### 3A: Analyse use case

1. Goal: Goal of the tool / workflow in one sentence. i.e. to support the user to calculate the total total cost of the project.
2. Model Use (Bim Uses): Please refer initially to the Mapping BIM uses, use cases and processes section in this document.

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

7. Describe the business value (How does it create value for your business/employer)
8. Describe the societal value (How does it make the world better)

* N.B. If it doesn't do either of these things (ideally it should do both - don't do it!!)

### 3E: Delivery

Requirements:
+ [x] **Markdown-formated report: Describing your tool/workflow: upload link to your Github report on Learn**

The report should link to or include:
- [x] An information exchange sheet  
- [x] Two IDM-diagrams
- [x] IFC model for the use case before the remodelling
- [x] IFC model for the use case after the remodelling
- [x] Description of and the script(s) used for the use case 

[BIM execution plan]: /41934/Concepts/BIMExecutionPlan
[BlenderBIM]: /41934/Concepts/BlenderBIM
