my_dog = {
    "name": "Frieda",
    "age": 5,
    "nicknames": ["Fru-Fru", "Lady McNugget"],
    "hungry": True,
}

del my_dog["hungry"]

if "hungry" in my_dog:
    print("The dog is hungry.")

capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin",
}

for state in capitals:
    print(f"The capital of {state} is {capitals[state]}.")
