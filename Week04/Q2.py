# Question 2: Two Sum

# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    # Outer loop
    for i in range(len(numbers)):
        # Inner loop
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)

    return None


# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    seen = {}  # Dictionary to store {number: index}

    for i in range(len(numbers)):
        needed = target - numbers[i]

        if needed in seen:
            return (seen[needed], i)

        seen[numbers[i]] = i

    return None


# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()