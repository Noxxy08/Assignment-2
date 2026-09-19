import random
random_numbers = [random.uniform(0, 10) for _ in range(5)]

print("Generated list of random numbers:")
print(random_numbers)

minimum_value = min(random_numbers)
maximum_value = max(random_numbers)

print(f"\nMinimum value: {minimum_value}")
print(f"Maximum value: {maximum_value}")