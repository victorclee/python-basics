# This code snippet is using a try-except block in Python to handle potential errors that may occur
# when converting user input to an integer.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
