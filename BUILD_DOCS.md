# How to build this documentation


1. Install UV and set up the environment:

First, install UV if you haven't already:
```console
# On macOS and Linux
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
$ powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install the project dependencies:
```console
$ uv pip install -e .
```

2. Build HTML-documentation:

On linux:

```console
$ make html
```

On Windows PowerShell:
```console
$ .\make.bat html
```

or

```console
$ sphinx-build -M html ./ _build/
```

3. Open `_build/html/index.html` in a web browser

## Alternative: Using pip (without UV)

If you prefer to use standard pip:
```console
$ pip install -e .
```
