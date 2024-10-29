def find_min_in_rotated_sorted(arr):
    # Edge case: if the list is empty
    if not arr:
        return None

    # If the list is not rotated or has only one element
    if arr[0] <= arr[-1]:
        return arr[0]

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if mid element is the minimum
        if arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        elif arr[mid - 1] > arr[mid]:
            return arr[mid]

        # Decide whether to search left or right
        if arr[mid] > arr[0]:  # Minimum is in the right half
            left = mid + 1
        else:  # Minimum is in the left half
            right = mid - 1

    return None  # In case there's no rotation (though we should handle this at the start)

# Test the function
arr = [30, 40, 50, 10, 20]
print("The minimum element in the rotated sorted list is:", find_min_in_rotated_sorted(arr))
