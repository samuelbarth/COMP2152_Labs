# Question 3: Shuffle the Array

def shuffle_array(nums, n):
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    
    second_half = nums[n:]   

    # Step 2: Create empty result list
    result = []

    # Step 3: Interleave using a for loop
    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result

# Test cases
test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()