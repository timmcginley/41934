# A5: Custom Tool

In this assignment we will develop a tool based on one of the use cases you identified in A3. The tool must:
* Address a specific use case
* ideally be written in python, but can be other approaches in special cases if agreed with the course responsible.

You will produce one final tool in the following folders, the structure of which is summarised below.

## 1. Input
You may include the code from the previous assignment to load the data from the IFC direct into your current tool. Alternatively you may want to load the data from the excel you have already generated in the previous assignment. In this case you should include the previous excel from assignment A4 in this folder.

Secondly you may also include the assumptions file from the previous assignment here.


## 2. Your tool
The tool should develop one of the use cases you identified in A3 and use the input you gained in A4.

## Submission structure 

This assumes that you are doing a normal python project.

Custom tool

- FOLDER: name of use case
  - FOLDER: model
    - duplex or something else (ifc)
  - FOLDER: input (this is in case you are importing some excel assumption data or regulations for instance)
    - excel data for instance.
  - FOLDER: output
    - this is if the output for your tool is a file, for instance an excel file.
  - main.py
  - FOLDER: documentation / readme.md file - you could use typora to edit.
    - Place the step by step guide to using your tool in here.
