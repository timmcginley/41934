# IfcOpenShell Installation

There are a couple of different ways of installing the IfcOpenShell python library.

# Use the built-in version in Blender/BlenderBIM.

The first one doesn't require you to install anything additional at all! Both Python and IfcOpenShell come with BlenderBIM already and can be used directly from the Blender Python console and text editor.

This article explaines how to both use the the interactive Python console and how to write full scripts in Blender with BlenderBIM Add-on: [https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on/Using_the_Python_console_with_BlenderBIM_Add-on](https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on/Using_the_Python_console_with_BlenderBIM_Add-on)

# Stand-alone installation
Writing and running scripts inside Blender is fine, but the text editor included with Blender is pretty basic. If you have to write longer scripts you might want the added functionalities that a dedicated code editor offers, like syntax highlighting, code hints, a debugger etc. 
To run scripts outside of Blender, you have to install Python, a code editor and any other libraries yourself.

You may want to write your file in an external code editor, but still run your script in Blender to have the visual connection to you model. To do that, follow [this tutorial](https://github.com/timmcginley/41934/blob/main/Concepts/BlenderBIM/E22_41934_How%20to%20run%20an%20external%20script%20in%20Blender.md) on running an external script in Blender. 

## Install Python
Install Python 3.10 or 3.11 from [https://www.python.org/downloads/](https://www.python.org/downloads/ "https://www.python.org/downloads/") (don't install 3.12 as IfcOpenShell might not be available for this version yet). If you have an older OS, you might need to install an older version, which is also fine.

## Install a code editor
You can install a very simple code editor like [Notepad++](https://notepad-plus-plus.org/downloads/) (only available for Windows), or a more modern editor like [Visual Studio Code](https://code.visualstudio.com/). 

## Install IfcOpenShell
Install `ifcopenshell` with one of the methods below.

### Install with pip
`ifcopenshell` is available through `pip`

So it can simply be installed by typing the following command in your command prompt or terminal:

`pip install ifcopenshell`

Follow this: [https://blenderbim.org/docs-python/ifcopenshell-python/installation.html#pypi](https://blenderbim.org/docs-python/ifcopenshell-python/installation.html#pypi)

### Install with Conda

If you have/are using (Ana)conda you can install ifcopenshell in your environment by running:

`conda install \-c ifcopenshell \-c conda\-forge ifcopenshell`

in your terminal or command prompt. See: [https://github.com/IfcOpenShell/IfcOpenShell#installing-ifcopenshell-with-conda](https://github.com/IfcOpenShell/IfcOpenShell#installing-ifcopenshell-with-conda "https://github.com/ifcopenshell/ifcopenshell#installing-ifcopenshell-with-conda") 

### Install manually through site-packages

You can also install IfcOpenShell by manually placing the folder in Python's `site-packages`  folder. 
Download the version that fits your operating system and Python version from [https://blenderbim.org/docs-python/ifcopenshell-python/installation.html#pre-built-packages](https://blenderbim.org/docs-python/ifcopenshell-python/installation.html#pre-built-packages) and follow further instructions from there.
