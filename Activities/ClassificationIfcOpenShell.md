# Classification in IfcOpenShell

We have a nearly complete classification system in IFC, why do we need classification systems in addition to IFC?

Standardisation is difficult and becomes more difficult the more things you try to standardise. Whilst the naming of things may seem a trivial problem, it does in fact get very complex very quickly as we when we name something in a set, we also classify it and say it is a type of one group and not another.

To take pressure from IFC it has been agreed that we are free to apply classification systems to it.

Examples include :
* Uniclass
* BIM7AA
* Many others

Pros and cons
- :white_check_mark: conforms to national / local naming norms.
- :x: naming different between different models from different places.
- :x: is that really what the entity? - is it classified properly?
- :x: if classified properly, is the ifc labling correct?
- :x: non trivial to translate between different classification systems.



## Classification in Blender / Bonsai

We can do that, its cool. We can also change stuff in there.

## Classification in IfcOpenShell

https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/classification/index.html



## Managers
* add the groups different classification rules to your script.

```python
classify = model.by_type('IfcClassification')[0]
```

## Code

## Analyst Code
* add the folowing code to your Rule check python script

```python
classify = model.by_type('IfcClassification')[0]
```


