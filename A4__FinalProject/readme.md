# Assignment 4

In this assignment we will focus on the input data that you need for your final tool / workflow. this data is either 

​	1. Found in the IFC

​	2. Found in external sources i.e. BR18

​	3. Based on assumptions (useful when we don't have the 'real' data that we need for our tool)

You will produce for the use case you defined in the [previous assignment](https://github.com/timmcginley/41934/tree/main/A3__UseCase):

## 1. Python script to produce Excel based on IFC
1. a python script to gather the data that you need for your project. This python script should produce an excel file containing the data from the IFC that you need in your project. for this we want you to:
* be careful about the naming of the sheets as this provides the hierarchy of information that you want to use in your tool.
* Alternatively, if you really don't want to use Python for this, assignment you can talk to Andrei.

## 2. Excel including assumptions and external data
* Some data may not be available in the model. In this case produce a second excel file that contains the assumptions for the use case...

* That second excel could also contain the external data that you need for your tool

## Submission structure 

Future formats

- FOLDER: name of use case 1
  - FOLDER: model
    - duplex or something else (ifc)
  - FOLDER: output
    - excel generated from python
    - excel file with assumptions and external information
  - main.py
- FOLDER: name of use case 2
  - FOLDER: model
    - duplex or something else (ifc)
  - FOLDER: output
    - excel generated from python
    - excel file with assumptions and external information
  - main.py

