def separate_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

# Example usage
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
even_list, odd_list = separate_even_odd(numbers)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
