# How to build this documentation


1. Install or update conda environment:
```console
$ conda env update -n docsEnv -f ./environment.yml
$ conda activate docsEnv
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
