capitals = {
    "California": {
        "capital": "Sacramento",
        "flowers": "California Poppy",
    },
    "New York": {
        "capital": "Albany",
        "flowers": "Rose",
    },
    "Texas": {
        "capital": "Austin",
        "flowers": "Bluebonnet",
    },
}

for state, facts in capitals.items():
    print(f"{state} - Capital: {facts['capital']}, Flower: {facts['flowers']}")
