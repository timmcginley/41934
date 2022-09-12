import ifcopenshell
import xlsxwriter # https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1

# this line opens the workbook, if it doesn't exist it makes it, otherwise
# it will overwrite the existing file.
# if it dpes already exist please close it otherwise it will not work (it cannot read open files)
workbook = xlsxwriter.Workbook('output/future_format.xlsx')
# you have the workbook open, now specify the sheet you want to write to
worksheet = workbook.add_worksheet()
# this is extra code that you can include to format the cells in your document. You could shange this to other examples. to create other effects.
bold = workbook.add_format({'bold': True})

# this line loads the ifc model into python. - careful most internet examples use ifc_model, 
# but we are using model here, so that it also works in RWTH viewer.
# When RWTH viewer loads the model in the GUI it calls it model.
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")

# this is normally formatted
worksheet.write(0,0, 'hello')

# in this line we have added the bold argument defined previously with the add_format command to define the format of the cell.
worksheet.write(0,0, 'hello', bold)

# when you have finished editing the document it is essential to close the workbook.
# these saves the document.
workbook.close()