# This code snippet is using a try-except block in Python to handle potential errors that may occur
# when converting user input to an integer.
# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Please enter a valid integer.")

try:
    1/0
    print("This will not print because of the error above.")
except TypeError:
    print("Error: Both inputs must be numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print("Done with try and except.")
