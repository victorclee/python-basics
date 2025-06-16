numbers = (1,2,3)

squares = []

for num in numbers:
    squares.append(num**2)

print(squares)

squares = [num**2 for num in numbers]

print(squares)
