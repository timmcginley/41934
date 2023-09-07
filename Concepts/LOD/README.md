# LOD (Level of ....)

>When starting in BIM there is a desire to model lots and a feeling that the more we model the more valuable the model will be and the better job we will have done. However it is not true. According to [iso 19650] the most important thing abotu BIM is not to model the maximum amount but actually the amount that is needed (and no more).
>
>Levels of (Detail / development) help us to be specific about what the Level of Information Need is

## Level of Information Need (LOIN)

LOD is tricky as it can mean different things. These can be summarised as LOX....

According to Dikon....
Level of Development (LOD) describes explicitly which information about model elements must be present in the BIM at different stages during the design and construction process. In Denmark this can be defined using DiKon.

LOD for building parts is comprised of: 
* Level of Reliability (LOR) describes the reliability of the information provided for the building part and it’s properties. 
* Level of Geometry (LOG) describes the building parts’ geometric representations and the extent of secondary components/parts.
* Level of Information (LOI) describes the building parts’ properties contained in, linked to, or in some other way connected.

In a recent thesis we realised that LOI is relatively easy to assess in a model based on DiKon but LOG and LOR are more difficult. If you select the Quality use case you could focus on how to get the LOI of the element and check this against the DiKon specification. 

However, whilst Dikon is common in Denmark, other countries use other definitions.

## Level of Detail
solves the problem of uncertainty about the level of detail to include in a model. For simplicity this course focuses on DIKON LOD guidelines, although this could be applied to other LOD specifications.

Indicates how much detail is included in the model element. It comprises the accuracy of a virtual shape representation when compared to the physical and functional characteristics of the actual object.

This session looks at the Dikon Guidelines and explores the concept of LOD in BIM.

## Level of Information (LoI)​
Indicates the non-graphical content in the BIM model at every stage of its development.

## Level of Development
LOD is the degree to which an element's geometry and attached information must be presented, or the degree of the level of information that project team members can rely on. Includes LOD and LOI.

$LoD+LoI=Level of Development (LOD)$

![image](https://github.com/timmcginley/41934/assets/1415855/2a2cc648-6e70-4639-a5a6-66ad2c46b1f9)

Image taken from the course documentation for the [IBIMD](https://www.ct.upt.ro/IBIMD/) project.

### LOD 100
Objects represented by symbols or simplified 3D, without indication of real physical geometry.

Modelling:​
* 2D drawing (plan, section or view), used to generate generic model of component detail or annotations;​
* 3D simple or imported from CAD software;​
* Generation of constructive details based on drawings already established in CAD software.​

Parameters:​
* It does not contain additional parameters and definitions of materials;​
* Non-parametric model.​

Quantitative:​
* It only counts the quantity and cost of objects entered in the model by categories and areas.​
  
Analysis:​
* Only the 3D drawing can be used for analysis of clash detection and construction execution plan.

### LOD 200
Objects graphically represented as a generic system. A simple representation of the real structure of the object.​

Modelling:​
* 2D drawing (plan, section or view), used to generate a generic component detail model that will be included in a family with the correct category;​
* 3D with the generic representation of the constructed element;​
Generation of constructive details through legends drawn in the template file itself.​

Parameters:​
* It does not contain additional parameters and materials definitions;​
* Objects with editable height, width and length.​

Quantitative:​
* It only counts the quantity and cost of objects entered in the model by categories and areas.​

Analysis:​
* Clash detection and construction execution plan.

### LOD 300/350
Objects are graphed more accurately in terms of quantity, size, shape, location, and orientation

Modelling:​
* 3D with exact representation of the shape of the built element but does not contain manufacturing or installation details;​
* Construction details generation through subtitles drawn in the template file.​

Parameters:​
* Contains additional information and visualization parameters, shared parameters and material definitions;​
* Objects with parameterization of dimensions according to the need of the element;​
* Object identification information such as manufacturer, model, cost, etc. can be added.​

Quantitative:​
* The categories and costs of the element can be composed, generating a more accurate table of quantities;​
* The shared parameters created in the family can serve as a basis for the preparation of the table of quantities.

### LOD 400
Objects represented in terms of size, shape, location, quantity and orientation, with details, fabrication, assembly and installation information​.

Modelling:​

3D with exact representation of the shape of the built element. The representation will aid in the development of details and tables.​

Parameters:​
* Additional information and visualization parameters, parameters shared and material definitions;​
* Model with parameterization of dimensions according to the need of the element;​
* Information to identify the element's manufacture, such as manufacturer, model, cost, etc.​

Quantitative:​
* The element's categories and costs can be composed, generating a more accurate quantitative table;​
* The shared parameters created in the family can serve as a basis for the preparation of the quantitative table in the project.​

Analysis:​
* Clash detection and construction execution plan.

### LOD 500
Corresponds to the As-Built Model​.

Modelling:​
* Updated 3D model according to As Built project.​

Parameters:​
* Parameters updated according to the As Built project.​

Quantitative:​
* Updated with the actual amounts spent during construction.​

Analysis:​
* Updated element assists in the management of facilities for the constructed building.

### Attribution:
This page is partly based on information from the [IBIMD](https://www.ct.upt.ro/IBIMD/) project of which DTU is a participant.

