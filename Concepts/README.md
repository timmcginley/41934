# OpenBIM Concepts

This course is possible because of a large community of humans who have been passionate about supporting standards in the AEC for a very long time. The main organisation representing these people and the needs for standardisaiton in the AEC is the awesome [BuildingSmart](https://www.buildingsmart.org/). BuildingSmart are responsible for the development of several core interoperability tools that make this course possible they include. The table below shows the 5 main standards supported by BuildingSMART. 

Dion Moult's summary of [OpenBIM and FOSS tools in the AEC](https://www.youtube.com/watch?v=h2Rv9iu7yDk&t=32s&ab_channel=DionMoult).

### IFC [Industry Foundation Classes](IFC/README.md)

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

### bSDD [buildingSMART Data Dictionary](bsDD/README.md)

*A standard library of general definitions of BIM objects and their attributes*

The buildingSMART Data Dictionary (bSDD) is an online service that hosts classifications and their properties, allowed values, units and translations. The bSDD allows linking between all the content inside the database. It provides a standardized workflow to guarantee data quality and information consistency.

### IdS [Information Delivery Specification](https://technical.buildingsmart.org/projects/information-delivery-specification-ids/)

*A computer interpretable document that defines the Exchange Requirements of model based exchange.*

The Information Delivery Specification defines how objects, classifications, properties, and even values and units need to be delivered and exchanged. This can be a combination of Industry Foundation Classes (IFC), Domain Extensions, and additional classifications and properties (national agreements or company specific ones; either stored in bSDD or somewhere else). This is the standard to use to define your Level of Information Needs. It brings validation of IFC to the client, the modeler and the Software Tools that perform (automated) analyses. It is a core component that can be used as a contract to deliver the correct information. It holds the ability to create localized and use-case specific requirements for your projects and asset portfolio. The IDS is the solution for predictable and reliable data exchange workflows.

![alt](https://technical.buildingsmart.org/wp-content/uploads/2020/07/ILS.png)

Technical info is available on https://github.com/buildingSMART/IDS
