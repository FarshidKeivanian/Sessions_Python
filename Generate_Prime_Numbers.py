def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Example usage
prime_numbers = generate_primes(100)
print("Prime numbers up to 100:", prime_numbers)

# Using primes to determine game level dimensions
level_width = prime_numbers[0]  # First prime number for width
level_height = prime_numbers[1]  # Second prime number for height

print(f"Game level dimensions: Width = {level_width}, Height = {level_height}")
