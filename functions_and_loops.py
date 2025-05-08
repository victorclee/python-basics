def shout_and_return(input_string):
    """Prints and returns the string in uppercase."""
    loud_input = input_string.upper()
    print(loud_input)
    return loud_input

for n in range(1, 4):
    shout_and_return('hello')

##help(shout_and_return)

##num = float(input("Enter a positive number: "))
##
##while num <= 0:
##    print("That's not a positive number!")
##    num = float(input("Enter a positive number: "))

