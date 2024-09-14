# Classification in IfcOpenShell

This activity explores the [classification] concept in [IfcOpenShell].

## Resources
https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/classification/index.html

## Prereqs
Completion of:
* The [Git(hub)] Activity including the cloning, adapting and running locally either manager or analyst scripts.
* [Classification in Blender] Activity

## Activity Decsription
* This activit

## Managers Code
* add the groups different classification rules to your script.

```python
classify = model.by_type('IfcClassification')[0]
```

## Analyst Code
* add the folowing code to your Rule check python script

```python
classify = model.by_type('IfcClassification')[0]
```

[classification]: /Concepts/Classification

[IfcOpenShell]: /Concepts/IfcOpenShell

[Git(hub)]: /Activities/GitIntro
[Classification in Blender]: /Activities/