import random

def coin_flip():
    """Simulate a coin flip."""
    if random.randint(0, 1) == 0:
        return 'heads'
    else:
        return 'tails'

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return 'heads'
    else:
        return 'tails'

heads_tally = 0
tails_tally = 0

for trial in range(100_000):
    result = unfair_coin_flip(0.2)
    if result == 'heads':
        heads_tally += 1
    else:
        tails_tally += 1

print(f"Heads: {heads_tally}, Tails: {tails_tally}")
