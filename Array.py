def has_zero_sum_sublist(arr):
    cumulative_sum = 0
    sum_set = set()

    for num in arr:
        cumulative_sum += num

        # Check if cumulative sum is zero or already exists in the set
        if cumulative_sum == 0 or cumulative_sum in sum_set:
            return True

        # Add the cumulative sum to the set
        sum_set.add(cumulative_sum)

    return False


# Test the function
arr = [4, 2, -3, 1, 6]
print("Sublist with sum zero exists:", has_zero_sum_sublist(arr))
