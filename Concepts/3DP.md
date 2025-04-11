# 3D Printing

We use 3D printing both in the deisgn prototyping stage and also as a construction technique.

This guide focuses on the first use of 3D printing as a deisgn testing tool.

## Getting started

There are lots of great videos for this. We are using Blender / Bonsai for this tutorial. This just contians some notes that might be useful to you to get you started.

There are 3 things to watch for when preparing your 3D models for printing.

* Remember that your 3d print will probably be scaled - most of the time we are not printing at 1:1
* 3D printing data can be provided in STL (mesh) or STEP files
* If mesh we can boolean them together, which can be useful
* If STEP we can see the different parts in the slicer software.

## Blender navigation
If you are new to this, save yourself a lot of trouble and turn on rotate around object.
```
Edit -> Preferences -> Navigation -> Toggle on: Orbit Around Selection
```

## To Blend or IFC
Either way if you safe your buidling model as an IFC or Blend file you will lose information when we starting doign teh boolean operations - so its probably betys to save a version of you model as a .blend file to prepare the 3d printable STL file. modre ifo here - https://docs.bonsaibim.org/guides/troubleshooting.html#incompatible-blender-features

## Boolean Tool

```
Edit -> Preferences -> Get Extensions -> Search for and install: 3D Print Toolbox
```

Shortcut: ctrl+shift+numpadplus


## Blender 3d print checking

```
Edit -> Preferences -> Get Extensions -> Search for and install: 3D Print Toolbox
```

## Export scale
In the blender STL export window you can scale your print to fit on the bed with the following units.

* 1:250 - 0.004
* 1:200 - 0.005
* 1:100 - 0.001
