# Working Together

This year we will try a new approach for your scripts.

Here is the template code you can use:

```python
# team_tool.py

def analyse(model):
    windows = model.by_type("IfcWindow")
    return {"window_count": len(windows)}

# this checks to see if it is running directly or has been called as a library.
if __name__ == "__main__":
    import ifcopenshell

    model = ifcopenshell.open("example.ifc")
    result = analyse(model)
    print(result)
```

If your own team runs it - 

```python
python team_tool.py
```

If the manager (runner) runs it - 

```python
from team_tool import analyse
result = analyse(my_model)
```
## Things to focus on 
* What useful data will you return?
* one clearly named callable function
* Each tool should have one primary 'C' function - see below.

## Functional classification

| Type        | Guiding Question                       | Examples                                                                                                                               |
|-------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Capture     | What information do we have?           | Extract room areas, column dimensions, wall layers or window quantities; read a reference table.                                       |
| Connect     | How does this information relate?      | Associate windows with rooms, walls with neighbouring spaces, new columns with existing supports, or materials with reference factors. |
| Calculate   | What can we derive?                    | Required airflow, glazing deficit, structural resistance, embodied carbon or cost.                                                     |
| Check       | Does the evidence satisfy a criterion? | Compare supplied airflow with demand, door width with a requirement, or façade materials with the stated intent.                       |
| Compare     | What changes between alternatives?     | Model revisions, window scenarios, material choices, or retention versus replacement.                                                  |
| Communicate | How do we make the findings useful?    | Tables, model highlights, charts and reports—including gaps, limitations and assumptions.                                              |
