data = ((1,2), (3,4))

for item in data:
    print(f"Row {data.index(item) + 1} sum: {sum(item)}")
