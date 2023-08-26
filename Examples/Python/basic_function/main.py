import ifcopenshell
# we will use the xlswriter library below to work with excel in python.
import xlsxwriter # https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1
# make a folder called output and then this line will make an 
# excel in there if one doesn't exist already
# N.B. remember to close the workbook if you have it open 
# BEFORE you run this script!
workbook = xlsxwriter.Workbook('output/test.xlsx')
# open the model as normally
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")
# this is a function it enables you to repeat the same command
# and reduce the amount of code that you have :)
# the function is called makeASheet - you can call it anything...
# it has a brackets after it, this is where the argument goes...
def makeASheet(ifcType):
    sheet = workbook.add_worksheet(ifcType)
    # define which row you want to start writing at.
    row =1
    for entity in model.by_type(ifcType):
        # this writes the data to the sheet
        # sheet.write(row, column, data)
        sheet.write(row,0,str(entity.Name))
        # this 'iterates' row so that each time we step down a row.
        # otherwise each new entry would overwrite the previous entry.
        row+=1
# here we can call the function and put it the argument
# in this case we are asking for the results of 
# different IFC entities to be written to their own sheets       
makeASheet('IfcSlab')
makeASheet('IfcWall')
makeASheet('IfcCovering')
makeASheet('IfcBeam')
# it is important to close the workbook afterwards
workbook.close()