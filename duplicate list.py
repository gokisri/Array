def find_duplicates(list1, list2, list3):
    # Convert each list to a set to get unique elements in each list
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    # Find common elements across all three sets
    duplicates = set1 & set2 & set3

    return list(duplicates) if duplicates else "No duplicates found"


# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 8, 9, 10]

result = find_duplicates(list1, list2, list3)
print("Duplicates across the three lists:", result)
