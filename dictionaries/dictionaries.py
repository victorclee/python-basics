capitals = {
  "California": "Sacramento",
  "New York": "Albany",
  "Texas": "Austin",
}

my_dog = {
    "name": "Frieda",
    "age": 5,
    "nicknames": ["Fru-Fru", "Lady McNugget"],
    "hungry": True,
}

print(my_dog["name"])

my_dog["Breed"] = "Poodle"

print(my_dog)

my_dog["age"] = 6

print(my_dog)

del my_dog["hungry"]

print(my_dog)
