# A1: IFC Dashboard

This assignment involves 4 steps

## 1) Export the standard Revit example project in IFC

The [link here](https://knowledge.autodesk.com/support/revit-products/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Revit-DocumentPresent/files/GUID-14037C31-EBAD-41A8-9099-E6DD65BB626E-htm.html) will help: 

So you probably want to know what version of IFC to export? The following is the advice from the IFA tool that we will be sending the IFC to in the next step.

IFC2x3 and IFC4 are supported, however, IFC4.0.n addendums and IFC4.n versions are not supported. See the IFC Documentation https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/ If the IFC file contains IFC4.0.n entities, those entities will not be processed and will not be listed as Entity types not processed on the File Summary worksheet.

I would recommend IFC2x3, to make it easier :)

## 2) Convert the IFC to an Excel work book using the IFA tool

[NIST tool download](https://www.nist.gov/services-resources/software/ifc-file-analyzer)

## 3) Explore the generated excel file and use this to try and understand the IFC standard

https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/

we will walk around the class to help you with this. it takes awhile to get your head around it...

## 4) Add a sheet to the work book you have generated, then use data from the other sheets to provide a dashboard of the building.

What you choose to represent in your dashboard is up to you. but you could consider trying to represent:

* areas of the building,

* quantities of materials,

* could you estimate cost? - if so how?

* what else can you find in the IFC data that you could use in your dashboard?

## 5) Submission

Your group must submit your modified excel including the dashboard sheet as the first sheet in the workbook.

You are not submitting any reports with this, so make sure that your dashboard is easy to understand - how do we know what we are looking at, and what you tried to do?



in the next assignment we look at how to apply this  approach using python..... See [example](https://github.com/timmcginley/11034/tree/main/Example%20files/Python/Working%20with%20excel)

