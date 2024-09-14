# Classification in Blender / Bonsai

This activity supports the [classification concept].

## Activity overview

* How to change the classification of the models.
* How are the models we are studying classified?


## Activity Description
There are many different types of classification in BIM. In this session we will try to map the elements we identify in the model to 2 different classification systems.

* CCS (Popular in Denmark)
* Uniclass (Popular in UK)
* OnmiClass (Popular in North America)


Overview video from Dion Moult here. Dion did not intend the video to be a tutorial so we have outlined the steps and required links below.

<https://www.youtube.com/watch?v=bWe8GDzVTVQ&ab_channel=DionMoult>

0. Make sure you have successfully added the [Bonsai] extension to Blender :)

1. Open the IFC file in Blender by going to File -> Open IFC Project 

2. Click on different model elements and see information about them in the Object Information tab on the panel towards the right (it looks like a box).

3. If you scroll down to the bottom you find Classification references. Their might not be a classification system currently in the IFC project. So...
4. Load a classification system.
Ifc Classification files are already included in your Blender / Bonsai installation and can be found by going to Edit -> Preferences -> Add-ons -> System:BlenderBIM -> Schema Directory. Otherwise they can be grabbed from here: <https://github.com/Moult/IfcClassification/tree/master/ifc>. Load it into BlenderBIM by going to Project Overview -> Project Setup -> Classifications and clicking on the little button called "Add Classification". Pick the Ifc Classification file from your computer and click the button called "Load Classification Library".

5. Click on any model object, go to the Object Information tab and add a classification under Classification References by picking the appropriate category from the tree.

6. Do this for at least 5 non-abstract model elements and 5 spaces (if you can find them - if not, do 5 more model elements) using either OmniClass, UniClass or CCS.




[Bonsai]: /Concepts/Bonsai

[classification]: /Concepts/Classification
