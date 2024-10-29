def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def find_happy_numbers(numbers):
    happy_numbers = [num for num in numbers if is_happy(num)]
    return happy_numbers, len(happy_numbers)

# Example usage
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_list, happy_count = find_happy_numbers(numbers)

print("Happy numbers:", happy_list)
print("Count of happy numbers:", happy_count)
