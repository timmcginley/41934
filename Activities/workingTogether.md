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
* Each tool should have one primary 'C' function - see below.
* one clearly named callable function i.e. if you are checking the axial load of the columns that would require:
    * CAPT_COL to get the columns
    * CALC_COL to calculate the columns and
    * CHEK_COL to test if this was ok and also maybe COMP_COL to compare them and or
    * COMM_COL to communicate results

```{note}
Sometimes it might not be necessary to create a different function for each element type - but we also shouldn't presume they can all be reused.
```

## Functional classification

| Type        |   Abreviation | Guiding Question                       | Examples                                                                                                               |
|-------------|--------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Capture     | CAPT | What information do we have?           | Extract room areas, column dimensions, wall layers or window quantities; read a reference table.                                       |
| Connect     | CONN | How does this information relate?      | Associate windows with rooms, walls with neighbouring spaces, new columns with existing supports, or materials with reference factors. |
| Calculate   | CALC | What can we derive?                    | Required airflow, glazing deficit, structural resistance, embodied carbon or cost.                                                     |
| Check       | CHEK | Does the evidence satisfy a criterion? | Compare supplied airflow with demand, door width with a requirement, or façade materials with the stated intent.                       |
| Compare     | COMP | What changes between alternatives?     | Model revisions, window scenarios, material choices, or retention versus replacement.                                                  |
| Communicate | COMM | How do we make the findings useful?    | Tables, model highlights, charts and reports—including gaps, limitations and assumptions.                                              |
