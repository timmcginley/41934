1) type in the cmd line

<pre>pip install xlsxwriter</pre>

2) in your python file  type

```
import ifcopenshell
import xlsxwriter # https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1

workbook = xlsxwriter.Workbook('output/future_format.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

ifc_file = ifcopenshell.open("model/Duplex_A_20110907.ifc")

worksheet.write(0,0, 'hello')

workbook.close()
```
