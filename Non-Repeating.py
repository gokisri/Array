def first_non_repeating_element(nums):
    count = {}

    # Count occurrences of each element
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Find the first element with a count of 1
    for num in nums:
        if count[num] == 1:
            return num

    return None  # Return None if there are no non-repeating elements


# Example usage
nums = [4, 5, 1, 2, 0, 4, 1, 2]
result = first_non_repeating_element(nums)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There are no non-repeating elements.")
