# Classification

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


>Classification systems attempt to solve the problem of non standard entity descriptions. They enable different countries and regions to have their own names for objects.

## Challenges / Issues
Managing the challenges of classification systems is a key component of the [manager] role in OpenBIM.
* Conversion between Classification systems.
* Model Classification completeness checking.
* Selecting the correct descrition with certainty.
* Choosing which classification system to specify for your project.
* knowing if an entity exists in a system.
* Where to put entities that *don't really fit*.

## Advanced Classification Problems
* Automated Classification. Use of Machine Learning to support the automated classification of building information models.

## Examples
* [Blender Classification]
* [IfcOpenShell Classification]


[manager]: /Roles/Manager
[modeller]: /Roles/Modeller

[Blender Classification]: /Activities/BlenderClassification
[IfcOpenShell Classification]: /Activities/IfcOpenShellClassification
