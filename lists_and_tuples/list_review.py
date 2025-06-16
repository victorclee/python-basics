food = ["rice", "beans"]

food.append("broccoli")

print(food)

food.extend(("bread", "pizza"))

print(food[0:2])

print(food[-1])

foods = "eggs, fruit, orange juice"
breakfast = foods.split(", ")

print(len(breakfast))
print(breakfast)

lengths = [len(item) for item in breakfast]
print(lengths)
