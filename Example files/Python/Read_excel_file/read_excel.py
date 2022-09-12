import xlrd
import ifcopenshell


## open the workbook
workbook = xlrd.open_workbook('output/future_format.xlsx')
## print the number of sheets in the workbook
print (workbook.nsheets)
## print the name of the sheets in the workbook
print (workbook.sheet_names())
## open the sheets by index - open the first sheet of the workbook
first_sheet = workbook.sheet_by_index(0)
## print the values in the first row of the first sheet
print (first_sheet.row_values(0))
## print the values in the first row of the first sheet
print (first_sheet.col_values(0))
## read the first cell in the first sheet
cell = first_sheet.cell(0,0)
## print the first cell
print (cell)
## print the value contained in the first cell
print (cell.value)


## more advanced example:

'''
For this example we take values from our assumptions sheet
based on the the global ids of the slabs in the model
'''

model = ifcopenshell.open("model/Duplex_A_20110907.ifc")

## Open the workbook
workbook = xlrd.open_workbook('output/future_format.xlsx')
## Open the assumptions sheet in the workbook
assumptions_sheet = workbook.sheet_by_index(4)

## loops though the stairs in the model
for slab in model.by_type('IfcSlab'):
    ## get the global id of the stair
    id = slab.GlobalId
    ## loops through the values in the first column of assumptionStair sheet
    for i in range(0, len(assumptions_sheet.col_values(0))):
        ##Get the cells in column A
        cell = assumptions_sheet.cell(i,0)
        ##Get the value of the cells
        value = cell.value
        ## Check if the value in the cell is the same as the global id of the slab
        if id == value:
            ## if the same id - print the value of the column B
            print(assumptions_sheet.cell(i,1).value)
