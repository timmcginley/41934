import ifcopenshell
import time
import pandas

# starting time
start = time.time()

#model = ifcopenshell.open("model/BIM_3W_Team05_Sub01.ifc")
model = ifcopenshell.open("model/Duplex_A_20110907.ifc")
end = time.time()

print()# total time taken
print(f"model load time is... {end - start}\n")