import copy

matrix = [[1,2], [3,4]]

the_matrix = copy.deepcopy(matrix)  # Creating a deep copy

print(id(matrix))
print(id(the_matrix))
print(id(matrix[0]))  # Original matrix
print(id(the_matrix[0]))  # Deep copied matrix

the_matrix[1] = ["Neo", "Trinity"]

print(matrix)  # Original matrix remains unchanged
print(the_matrix)  # Modified matrix copy

the_matrix[0][0] = "Morpheus"  # Modifying an element in the first row
print(the_matrix)  # Modified deep copy
print(matrix)  # Original matrix remains unchanged
