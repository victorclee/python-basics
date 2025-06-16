data = ((1,2), (3,4))

for item in data:
    print(f"Row {data.index(item) + 1} sum: {sum(item)}")

numbers = [4,3,2,1]
more_numbers = numbers[:]
numbers.sort()
print(f"Sorted numbers: {numbers}")
print(f"More numbers (copy): {more_numbers}")
