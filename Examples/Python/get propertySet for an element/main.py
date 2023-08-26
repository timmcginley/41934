import ifcopenshell

model = ifcopenshell.open('model\Duplex_A_20110907.ifc')

# this just gets you the entity, defined here as wall
# feel free to change this to your needs
wall = model.by_type('IfcWall')[0]
for definition in wall.IsDefinedBy:
	# To support IFC2X3, we need to filter our results.
	if definition.is_a('IfcRelDefinesByProperties'):
		property_set = definition.RelatingPropertyDefinition
		# Might return Pset_WallCommon
		print(property_set.Name)

# ###################### end of example ###########################
