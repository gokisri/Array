def find_triplet(arr, target_sum):
    arr.sort()  # Sort the array
    n = len(arr)

    # Iterate through the array
    for i in range(n - 2):
        # Use two pointers to find the triplet
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target_sum:
                return arr[i], arr[left], arr[right]  # Triplet found
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return None  # No triplet found

# Test the function
arr = [10, 20, 30, 9]
target_sum = 59
result = find_triplet(arr, target_sum)
if result:
    print("Triplet with sum", target_sum, "is:", result)
else:
    print("No triplet with the given sum found.")
