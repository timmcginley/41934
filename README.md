# 41934 Advanced BIM

Advanced BIM enables you to get the information you need to analyse and design building systems in your disciplinary specialism. This requires interoperability and standardisation; therefore this course focuses on Open BIM data and standards. Excitingly there is an emerging emerging ecosystem of OpenBIM tools supported by IfcOpenShell for instance that are starting to provide an OpenBIM alternative to contemporary inoperable closed BIM tools and data. We believe that University education has a responsibility to support the transition in the AEC to OpenBIM data and standards.  To achieve this, the Advanced BIM course at DTU therefore supports five emerging OpenBIM roles including: modelling, analysis tool development, management/coordination and ontology development. The aim of the course is to support you to become an OpenBIM expert (guru) in your chosen role(s) in the course supported by your disciplinary expertise i.e. LCA or structural analysis for instance. At the end of the course your group is required to develop a tutorial to teach one of these concepts to a group of peers to demonstrate your expertise in the area. The course has three main principles.
1) Think in ‘IFC, FAIR data and Open Standards’
2) Support the circularity of data, knowledge, processes, models and tools
3) Build (Architect) OpenBIM tools for specific use cases that applies domain expertise.

The course is divided into 5 modules, each module builds on the previous one to guide you through identifying your use case and the data you need to analyse to create your tool or workflow. The course focuses on the IFC schema to provide you with a robust, future proof and interoperable understanding of BIM.

## Course Calender
Overview of teh course is available [here](/Schedule)

## Assignments
1. [LearningFromOpenBIM](/Assignments/A1__OpenBIM)
2. [FutureBIM](/Assignments/A2__FutureBIM)
3. [UseCase](/Assignments/A3__UseCase)
4. [FinalProject](/Assignments/A4__FinalProject)
5. [ProjectReflection](/Assignments/A5__ProjectReflection)

## Learning Objectives
The course learning objectives are organised into three main priniciples.
### Principle 1. Think in ‘IFC, FAIR data and Open Standards’
1. Develop a BIM Execution Plan for a specific use case based on the OpenBIM standard ISO 19650.
2. Identify, locate and extract information for a specific use case from an IFC model.
3. Apply appropriate OpenBIM standards and guidelines to support open and FAIR data, tools and processes in a specific use case.
4. Provide professional disciplinary guidance based on OpenBIM analysis for a specific use case.
### Principle 2. Support the circularity of data, knowledge, processes, models and tools
5. Develop expertise in two of four OpenBIM roles (Modelling, Analysis tool development, management / coordination or Ontologist)
6. Create, Fork, branch and collaborate with peers in a code repository.
7. Identify BIM challenges by analysing OpenBIM data (i.e. IFC files and project reports from previous advanced building design projects or models produced by peers in this course).
8. Teach an advanced BIM concept you have learnt in the course to your peers.
### Principle 3. Build (Architect) OpenBIM tools for specific use cases that applies domain expertise.
9. Identify and model a BIM use case based on the BIM challenges identified from analysis of an OpenBIM project in BPMN.
10. Identify an appropriate development methodology for an OpenBIM tool or model to satisfy the identified use case.
11. Apply and improve programming skills in Python to develop an OpenBIM tool or modelling skills in OpenBIM using your engineering domain expertise to address a specific use case.
12. Evaluate software licensing suitability and implications for the OpenBIM tool you develop or modelling tool you use.

## Focus on problems you care about
This course has been designed so that the emphasis is on learning FROM BIM rather than learning HOWTO BIM [(McGinley & Krijnen, 2021)](https://itc.scix.net/paper/w78-2021-paper-070). However it is not possible to support every possible use case, therefore the course focuses on the following:

* LCA
* Structure
* Cost
* Indoor & Energy
* Acoustic
* Daylight

## OpenBIM

This course is possible because of a large community of humans who have been passionate about supporting standards in the AEC for a very long time. The main organisation representing these people and the needs for standardisaiton in the AEC is the awesome [BuildingSmart](https://www.buildingsmart.org/). BuildingSmart are responsible for the development of several core interoperability tools that make this course possible they include. The table below shows the 5 main standards supported by BuildingSMART. 

### IFC [Industry Foundation Classes](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/)

*An industry-specific data model schema*

IFC is a standardized, digital description of the built asset industry.  It is an open, international standard ([ISO 16739-1:2018](https://www.iso.org/standard/70303.html)) and promotes vendor-neutral, or agnostic, and usable capabilities across a wide range of hardware devices, software platforms, and interfaces for many different use cases.

* [IFC History](https://itc.scix.net/pdfs/w78-2015-paper-004.pdf)
* [Industrial Foundation Classes paper](https://publications.cms.bgu.tum.de/books/bim_2018/06_IFC_07.pdf)

### IDM [Information Delivery Manual](https://www.buildingsmart.org/standards/bsi-standards/information-delivery-manual/)

*A methodology for defining and documenting business processes and data requirements*

The built asset industry is characterized by bringing many different stakeholders together in a project-specific organization. In order to work efficiently, it is necessary for all participants to know which and when different kinds of information have to be communicated. The **ISO 29481-1:2010** “Building Information Modelling - Information Delivery Manual - Part 1: Methodology and Format” standard has been developed by buildingSMART in order to have a methodology to capture and specify processes and information flow during the lifecycle of a facility. 

More information is found [here](https://technical.buildingsmart.org/resources/information-delivery-manual/)

### MVD [Model View Definitions](https://www.buildingsmart.org/standards/bsi-standards/model-view-definitions-mvd/)

*Data model exchange specifications*

Model View Definitions (MVDs) are buildingSMART’s solution to create IFC based standards that can be implemented and tested. A great idea to produce a subset of the total model represented in the IFC. The idea would be to create a smaller specific model that captures just the information they need. The reality is that this is quite difficult to produce which it is possible is the reason there are few approved MVD instances.

An MVD consists of three main components:  

1. A set of Concept Templates. These concept templates define additional agreements on how to use the IFC Schema.
2. A set of Exchange Requirements. This is a selection of entities and properties from the IFC Schema that are found suitable for a selection of use-cases.
3. A description on how Software should deal with the data that are exchanged. For example, can the software use the data as a reference, or should the data be mapped to internal objects during import.

### BCF [BIM Collaboration Format](https://www.buildingsmart.org/standards/bsi-standards/bim-collaboration-format-bcf/)

*Model-based, software-independent communication protocols*

The BIM Collaboration Format (BCF) allows different BIM applications to communicate model-based issues with each other by leveraging IFC models that have been previously shared among project collaborators.  BCF was created for facilitating open communications and improving IFC-based processes to more readily identify and exchange model-based issues between BIM software tools, bypassing proprietary formats and workflows.

A detailed explanation of BCF can be found [here.](https://technical.buildingsmart.org/standards/bcf/)

### bSDD [buildingSMART Data Dictionary](https://www.buildingsmart.org/users/services/buildingsmart-data-dictionary/)

*A standard library of general definitions of BIM objects and their attributes*

The buildingSMART Data Dictionary (bSDD) is an online service that hosts classifications and their properties, allowed values, units and translations. The bSDD allows linking between all the content inside the database. It provides a standardized workflow to guarantee data quality and information consistency.

### IdS [Information Delivery Specification](https://technical.buildingsmart.org/projects/information-delivery-specification-ids/)

*A computer interpretable document that defines the Exchange Requirements of model based exchange.*

The Information Delivery Specification defines how objects, classifications, properties, and even values and units need to be delivered and exchanged. This can be a combination of Industry Foundation Classes (IFC), Domain Extensions, and additional classifications and properties (national agreements or company specific ones; either stored in bSDD or somewhere else). This is the standard to use to define your Level of Information Needs. It brings validation of IFC to the client, the modeler and the Software Tools that perform (automated) analyses. It is a core component that can be used as a contract to deliver the correct information. It holds the ability to create localized and use-case specific requirements for your projects and asset portfolio. The IDS is the solution for predictable and reliable data exchange workflows.

![alt](https://technical.buildingsmart.org/wp-content/uploads/2020/07/ILS.png)

Technical info is available on https://github.com/buildingSMART/IDS

## Code examples
The super exciting thing about this course is that it tries to move from the old way of running linear courses, where students repeat the same standard exercise each year and try and change it.

## Course information booklets

The information booklets are in the process of being converted to markdown. In the mean

##  BIM Awesome

We are at an exciting point in BIM at the moment, it is a real moment where the future is being defined in front of our eyes. We are trying to bring together some of these developments in a list repo called [bim awesome](https://dtu-byg.github.io/BIM-awesome/).
