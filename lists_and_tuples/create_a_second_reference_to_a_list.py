# matrix = [[1,2], [3,4]]

# print(matrix)

# the_matrix = matrix

# print(the_matrix)

# the_matrix[1] = ["Neo", "Trinity"]

# print(matrix)

# print(id(matrix))
# print(id(the_matrix))

matrix = [[1,2], [3,4]]

the_matrix = matrix[:] # Creating a shallow copy

print(id(matrix))
print(id(the_matrix))

the_matrix[1] = ["Neo", "Trinity"]

print(matrix)  # Original matrix remains unchanged
print(the_matrix)  # Modified matrix copy

the_matrix[0][0] = "Morpheus"  # Modifying an element in the first row
print(the_matrix)
print(matrix)  # Original matrix is affected because it's a shallow copy

print(id(matrix[0]))
print(id(the_matrix[0]))

# Shallow copies contain copied references. They don't copy the objects themselves.
