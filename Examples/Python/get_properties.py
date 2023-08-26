## Run script in blender
import bpy
from blenderbim.bim.ifc import IfcStore

file = IfcStore.get_file()


### GET PROPERTIES ###

## Get attributes directly from the element
spaces = file.by_type("IfcSpace")

for space in spaces:
    print(space.LongName)

## go through all the beams in the model
beams = file.by_type("IfcBeam")

for beam in beams:
    beam.Name
    ## get property sets attached to beams through IsDefinedBy"
    for definition in beam.IsDefinedBy:
        
        ## To support IFC2X3, we need to filter our results.
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            
            
            ## Sort by the name of the propertySet
            if property_set.Name == "Pset_BeamCommon":
               for property in property_set.HasProperties:
                    
                    #print(property)
                    ## sort b the name of the property
                    if property.Name == "IsExternal":
                        print(property.NominalValue.wrappedValue)

### GET MATERIALS ###

## Through HasAssociations get the associated materials of the element
for beam in beams:
    for relAssociatesMaterial in beam.HasAssociations:
        print(relAssociatesMaterial.RelatingMaterial.Name)


### GET RELATING STRUCTURE ###

## Through ContainedInStructure get the inverse relation to the 
for beam in beams:
    for relContainedInSpatialStructure in beam.ContainedInStructure:
        print(relContainedInSpatialStructure.RelatingStructure.Name)