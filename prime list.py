def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers, len(prime_numbers)

# Example usage
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_list, prime_count = find_primes(numbers)

print("Prime numbers:", prime_list)
print("Count of prime numbers:", prime_count)
