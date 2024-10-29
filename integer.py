def sum_first_last(number):
    number_str = str(abs(number))  # Convert number to string and handle negative numbers
    first_digit = int(number_str[0])  # First character in string
    last_digit = int(number_str[-1])  # Last character in string
    return first_digit + last_digit

# Example usage
number = 351
result = sum_first_last(number)
print(f"The sum of the first and last digits of {number} is: {result}")
