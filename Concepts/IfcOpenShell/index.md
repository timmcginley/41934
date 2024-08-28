# IfcOpenShell

```{toctree}
:hidden:
:glob:
*
*/index
installation/*
```

*IfcOpenShell solves the problem of enabling the extraction, manipulation, and analysis of Building Information Modeling (BIM) data from Industry Foundation Classes (IFC) files.*

It is an open source ([LGPL](https://github.com/IfcOpenShell/IfcOpenShell/tree/master/COPYING.LESSER "LGPL-3.0-or-later")) software library and tookit available in both C++ and Python. In addition to a C++ and Python API, IfcOpenShell comes with an ecosystem of tools, including libraries and CLI apps for converting IFC models to other formats (IfcConvert), comparing changes between files (IfcDiff), clash detection (IfcClash), creating and auditing IDS and BCF files (IfcTester and bcf) and many others. 
IfcOpenShell also provides the basis for BlenderBIM. Much of BlenderBIM's functionality can be thought of as a GUI (graphical user interface) to IfcOpenShell.

IfcOpenShell is very closely based on the IFC schema, so for documentation of the methods used in the library, the IFC documentation itself can be very useful. Other than that, the many tutorials and examples and the IfcOpenShell-Python documentation are good places to start. See references to IfcOpenShell tutorials and examples under [IfcOpenShell Basic Examples](/Examples/IfcOpenShell/Basic) page.

This tutorial site bundles tutorials on IfcOpenShell, including the collection of small reference scripts and how to execute them. This repository is work in progress, so please be flexible and patient with scripts that are not working properly. Your suggestions are also hugely appreciated in the Issues tab!

## Learn IfcOpenShell

- [Installing and Getting Started](installation/updated_installation_instructions/)
- Check out the exmaples [here](/Examples/IfcOpenShell/)
- Selecting elements of a particular type
- Retrieve attributes
- Retrieve properties
- Exporting data to CSV
- Importing and loading data
- Create new Element

## And then....

Upon completing this, you could:
- Check out a tutorial on identifying relevant [BIM use cases](https://github.com/DTU-Byg/BIM-USE) and developing IfcOpenShell tools in Python to address these.

# References:
- IfcOpenShell Github-page: [https://github.com/IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
- IfcOpenShell website: [http://ifcopenshell.org/](http://ifcopenshell.org/)
- IfcOpenShell-Python library documentation: [https://ifcopenshell.github.io/docs/python/html/py-modindex.html](https://ifcopenshell.github.io/docs/python/html/py-modindex.html)
- IfcOpenShell-Python API documentation: [https://blenderbim.org/docs-python/autoapi/index.html](https://blenderbim.org/docs-python/autoapi/index.html)
- IFC 4x3 documentation: [https://ifc43-docs.standards.buildingsmart.org/](https://ifc43-docs.standards.buildingsmart.org/)
