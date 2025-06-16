captains = {
  "Enterprise": "Picard",
  "Defiant": "Sisko",
  "Voyager": "Janeway",
}

if "Enterprise" in captains:
    print("The Enterprise is captained by", captains["Enterprise"])
    
if "Discovery" not in captains:
    captains["Discovery"] = "Unknown"
  
print(captains)

for ship in captains:
    print(f"The captain of the {ship} is {captains[ship]}")

del captains["Discovery"]

print("After removing Discovery:", captains)
