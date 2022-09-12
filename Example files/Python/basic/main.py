import ifcopenshell
import time

# starting time
start = time.time()

model = ifcopenshell.open("model/BIM_3W_Team05_Sub01.ifc")
#model = ifcopenshell.open("model/Duplex_A_20110907.ifc")
end = time.time()

# total time taken
print(f"model load time is... {end - start}\n")

building = model.by_type('IfcBuilding')


def elCount(entityName,ifcClass):
    print("{} = {}".format(entityName,len(model.by_type(ifcClass))))
    
elCount("floors",'IfcBuildingStorey')   
elCount("beams",'IfcBeam')   
elCount("specialWalls",'IfcWall')
slabVol = 0
slab =model.by_type('IfcSlab')[0]
print(slab.IsDefinedBy)

elCount("standardWalls",'IfcWallStandardCase')
elCount("windows",'IfcWindow')  
elCount("doors",'IfcDoor')     
elCount("slabs",'IfcSlab')      

elevation = -20000
f2f = 0
floors = model.by_type('IfcBuildingStorey')

for floor in floors[::-1]:
    print ("\n_____ {} - {}".format(floor.Name,floor.Elevation))
    # get the f2f for the storey
    for relDefinesByProperties in floor.IsDefinedBy:
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
            #and then get the attribute we are looking for
            if prop.Name == 'height':
                #add the length to the total length
                print("found it!")
                f2f = prop.NominalValue.wrappedValue
            else:
                print("didn't find it! "+prop.Name+" : "+str(prop.NominalValue.wrappedValue))
    print(str(f2f)+"KDFKDFKMFGF----HK")
    for space in floor.IsDecomposedBy:

        for inst in space.RelatedObjects:
            print(inst)

