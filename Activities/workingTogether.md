# Working Together

This year we will try a new approach for the scripts

Here is the template code you can use:

```python
# team_tool.py

def analyse(model):
    windows = model.by_type("IfcWindow")
    return {"window_count": len(windows)}

# this checks to see if it is
if __name__ == "__main__":
    import ifcopenshell

    model = ifcopenshell.open("example.ifc")
    result = analyse(model)
    print(result)
```

The if __name__ == "__main__": argument checks to see if it is running directly or has been called as a library.

so if your own team runs it - 

```python
python team_tool.py
```

so if the manager runs it - 

```python
from team_tool import analyse
result = analyse(my_model)
```
