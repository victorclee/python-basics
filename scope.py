# Local scope
# def print_total():
#   total = 0
#   print(f"From function: {total=}")

# print_total()
# print(f"{total=}")

# Enclosing scope
# def print_total():
#     def inner_print_total():
#         print(f"From inner function: {total=}")

#     total = 0
#     inner_print_total()
#     print(f"From function {total=}")    

# print_total()

# Global scope
# def print_total():
#     def inner_print_total():
#         total = 7
#         print(f"From inner function: {total=}")

#     total = 12
#     inner_print_total()
#     print(f"From function {total=}")    

# total = 5
# print_total()
# print(f"From global: {total=}")

# Global keyword
# counter = 0

# def update_counter():
#     global counter # bad practice
#     counter = counter + 1
    
# update_counter()
# print(counter)

# Use local names rather than global names
# Write self-contained functions
# Try to use unique object names, no matter what scope you are in
# Avoid global name modifications throughout your programs

counter = 0

def update_counter(current__counter):
    return current__counter + 1 

counter = update_counter(counter)
print(counter)
