# Classification in IfcOpenShell

This activity explores the [classification] concept in [IfcOpenShell].

## Resources
[Ifcopenshell - Classification](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/classification/index.html)

## Prereqs
Completion of:
* The [Git(hub)] Activity including the cloning, adapting and running locally either manager or analyst scripts.
* [Classification in Blender] Activity


## Code snippets

### Identify classification schemas used in model

Identify all classification systems used in the model:

```python
import ifcopenshell
import ifcopenshell.util.classification
...
...
...
classifications = model.by_type("IfcClassification")
print("Classifications:", classifications)
```

### Find classification information for an element

Find all classification references for an element:

```python
element = ...

references = ifcopenshell.util.classification.get_references(element)
for reference in references:
    system = ifcopenshell.util.classification.get_classification(reference)
    print("This reference is part of the system", system.Name)
    print("The element has a classification reference of", reference.Identification)
```


## Activity Decsription
* This activit

## Managers Code
* add the groups different classification rules to your script.


## Analyst Code
* add the folowing code to your Rule check python script

[classification]: /Concepts/Classification

[IfcOpenShell]: /Concepts/IfcOpenShell/index

[Git(hub)]: /Activities/GitIntro
[Classification in Blender]: /Activities/BlenderClassification