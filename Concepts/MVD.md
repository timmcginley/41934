### MVD [Model View Definitions](https://www.buildingsmart.org/standards/bsi-standards/model-view-definitions-mvd/)

*Data model exchange specifications*

It is a subset of IFC schema, which is used to organize and indicate selected data in a model that meets specific criteria or data flow. MVD makes it easy to extract the necessary information predetermined from an IFC. Furthermore, MVD aims to limit the amount of information extracted from an IFC file based on the recipient's requirements and the specific workflow.

Model View Definitions (MVDs) are buildingSMART’s solution to create IFC based standards that can be implemented and tested. A great idea to produce a subset of the total model represented in the IFC. The idea would be to create a smaller specific model that captures just the information they need. The reality is that this is quite difficult to produce which it is possible is the reason there are few approved MVD instances.

An MVD consists of three main components:  

1. A set of Concept Templates. These concept templates define additional agreements on how to use the IFC Schema.
2. A set of Exchange Requirements. This is a selection of entities and properties from the IFC Schema that are found suitable for a selection of use-cases.
3. A description on how Software should deal with the data that are exchanged. For example, can the software use the data as a reference, or should the data be mapped to internal objects during import.
