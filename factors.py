# input = int(input("Enter a number: "))
# print(input)
# number = 1

# while number < input:
#     if input % number == 0:
#         print(f"{number} is a factor of {input}")
#     number += 1


def find_factors(number):
    """Find all factors of a given number."""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    try:
        num = int(input("Enter a number: "))
        factors = find_factors(num)
        for factor in factors:
            print(f"{factor} is a factor of {num}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
