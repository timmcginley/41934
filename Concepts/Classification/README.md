# Classification

>Classification systems attempt to solve the problem of non standard entity descriptions. They enable different countries and regions to have their own names for objects.

## Challenges / Issues
Managing the challenges of classification systems is a key component of the [manager] role in OpenBIM.
* Conversion between Classification systems.
* Model Classification completeness checking.
* Selecting the correct descrition with certainty.
* Choosing which classification system to specify for your project.
* knowing if an entity exists in a system.
* Where to put entities that *don't really fit*.

Advanced Classification Problems
* Automated Classification. Use of Machine Learning to support the automated classification of building information models.

## Exercise: Classification in BlenderBIM

There are many different types of classification in BIM. In this session we will try to map the elements we identify in the Skylab model to 2 different classification systems.

* CCS (Popular in Denmark)
* Uniclass (Popular in UK)
* OnmiClass (Popular in North America)


Overview video from Dion Moult here. Dion did not intend the video to be a tutorial so we have outlined the steps and required links below.

<https://www.youtube.com/watch?v=bWe8GDzVTVQ&ab_channel=DionMoult>

1) Open the Skylab IFC file in BlenderBIM by going to File -> Open IFC Project
2) Click on different model elements and see information about them in the Object Information tab on the panel towards the right (it looks like a box).
3) Load a classification system.
Ifc Classification files are already included in your BlenderBIM installation and can be found by going to Edit -> Preferences -> Add-ons -> System:BlenderBIM -> Schema Directory. Otherwise they can be grabbed from here: <https://github.com/Moult/IfcClassification/tree/master/ifc>. Load it into BlenderBIM by going to Project Overview -> Project Setup -> Classifications and clicking on the little button called "Add Classification". Pick the Ifc Classification file from your computer and click the button called "Load Classification Library".
4) Click on any model object, go to the Object Information tab and add a classification under Classification References by picking the appropriate category from the tree.
5) Do this for at least 5 non-abstract model elements and 5 spaces.





[manager]: /41934/Roles/Manager
[modeller]: /41934/Roles/Modeller
