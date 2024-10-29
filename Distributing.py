def min_difference(mango_bags, M):
    # Sort the bags to facilitate finding the minimum difference
    mango_bags.sort()

    n = len(mango_bags)

    # If there are fewer bags than students, return -1
    if n < M:
        return -1

    # Initialize the minimum difference to a large value
    min_diff = float('inf')

    # Iterate over the bags, looking for the minimum difference
    for i in range(n - M + 1):
        current_diff = mango_bags[i + M - 1] - mango_bags[i]
        min_diff = min(min_diff, current_diff)

    return min_diff


# Example usage
mango_bags = [12, 34, 21, 56, 45, 32]
M = 3
result = min_difference(mango_bags, M)

if result != -1:
    print(f"The minimum difference between the maximum and minimum mangoes in the bags is: {result}")
else:
    print("Not enough bags for the students.")
