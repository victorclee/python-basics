matrix = [[1,2], [3,4]]

print(matrix)

the_matrix = matrix

print(the_matrix)

the_matrix[1] = ["Neo", "Trinity"]

print(matrix)

print(id(matrix))
print(id(the_matrix))
