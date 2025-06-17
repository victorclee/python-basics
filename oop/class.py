# constructor and attributes
class Point:
    ''' A class to represent a point in 2D space. '''
    dimensions = 2  # class attribute
    def __init__(self, x, y): # constructor
        self.x = x
        self.y = y
    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
    def __str__(self):
        return f"Point at x:{self.x}, y:{self.y}"
class Doggo:
    ''' A class to represent a dog. '''
    species = "Canis familiaris"  # class attribute
    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute
    def description(self):
        return f"{self.name} is {self.age} years old, and is a good doggo."
    def speak(self, sound):
        return f"{self.name} says {sound}!"
    def __str__(self):
        return f"{self.name} is {self.age} years old."
