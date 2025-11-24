# Introduction to scripting with Ifcopenshell in system environment

In this activity you will set up the necessary environment for development using [Python] and [IfcOpenShell].
You will create a minimal script counting the amount of walls found in a given [IFC-STEP] model.

Knowledge of [Python] is assumed.

## Preparing development environment

For this course, we recommend using UV for fast Python package management. Anaconda is also supported for advanced users who prefer it.

Detailed instructions for installation is available at [Install Ifcopenshell](https://docs.ifcopenshell.org/ifcopenshell-python/installation.html).

- Make sure you have an appropriate text-editor installed. [Vscode](https://code.visualstudio.com/) is recommended.
- Make sure you have a recent version of Python installed. Python `3.11` is recommended.
- Install `ifcopenshell` either by:
    - PIP: In your [CLI] run `pip install ifcopenshell`.
    - UV: Run `uv pip install ifcopenshell` for faster installation.
    - Conda: `conda install -c conda-forge ifcopenshell pythonocc-core`. This includes [OpenCascade](https://github.com/tpaviot/pythonocc-core) which may be useful for geometric operations further down the road.

## Hello `ifcopenshell`

Here is a minimal example counting the amount of wall entities found in a model:

```python
import ifcopenshell
model = ifcopenshell.open('/path/to/your/model.ifc')

walls = model.by_type('IfcWall')
print(f"Walls in model: {len(walls)}")
```

Save the above code in a `.py` file and then execute it.
Watch the command line output to read the wall count.

```{attention}
Beware of absolute and relative file paths!
If pointing to your model using a relative path, the path is relative to the working directory _of which you are executing the code_, and not the path of the `.py` file itself.
```
[CLI]: /Concepts/CommandLine
[Python]: /Concepts/Python
[IfcOpenShell]: /Concepts/IfcOpenShell
[IFC-STEP]: /Concepts/IFC



