input = int(input("Enter a number: "))
print(input)
number = 1

while number < input:
    if input % number == 0:
        print(f"{number} is a factor of {input}")
    number += 1
