# constructor and attributes
class Point:
    dimensions = 2  # class attribute
    def __init__(self, x, y): # constructor
        self.x = x
        self.y = y

class Doggo:
    species = "Canis familiaris"  # class attribute
    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute
