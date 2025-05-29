# ValueError: This code will raise a ValueError because "Hello" cannot be converted to an integer.
# int("Hello")
# Result:
# Traceback (most recent call last):
#   File "/Users/victorclee/Documents/learning/Python/recovering_from_errors.py", line 1, in <module>
#     int("Hello")
# ValueError: invalid literal for int() with base 10: 'Hello'

# TypeError: This code will raise a TypeError because you cannot concatenate a string and an integer.
# "1" + 2
#  Result:
# Traceback (most recent call last):
#   File "/Users/victorclee/Documents/learning/Python/recovering_from_errors.py", line 9, in <module>
#     "1" + 2
#     ~~~~^~~
# TypeError: can only concatenate str (not "int") to str

# NameError: This code will raise a NameError because the variable `does_not_exist` has not been defined.
# print(does_not_exist)
# Result:
# Traceback (most recent call last):
#   File "/Users/victorclee/Documents/learning/Python/recovering_from_errors.py", line 18, in <module>
#     print(does_not_exist)
#           ^^^^^^^^^^^^^^
# NameError: name 'does_not_exist' is not defined

# ZeroDivisionError: This code will raise a ZeroDivisionError because you cannot divide by zero.
1/0
# Result:
# Traceback (most recent call last):
#   File "/Users/victorclee/Documents/learning/Python/recovering_from_errors.py", line 27, in <module>
#     1/0
#     ~^~
# ZeroDivisionError: division by zero
