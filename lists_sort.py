colors = ["red", "yellow", "green", "blue"]

colors.sort()  # Sorts the list in place

print(colors)  # Output: ['blue', 'green', 'red', 'yellow']

numbers = [1, 10 , 5, 3]

numbers.sort()  # Sorts the list in place 

print(numbers)  # Output: [1, 3, 5, 10]

colors.sort(reverse=True)  # Sorts the list in place in reverse order
numbers.sort(reverse=True)  # Sorts the list in place in reverse order
print(colors)  # Output: ['yellow', 'red', 'green', 'blue']
print(numbers)  # Output: [10, 5, 3, 1] 

colors.sort(key=len)  # Sorts the list by length of the strings
print(colors)  # Output: ['red', 'blue', 'green', 'yellow']
