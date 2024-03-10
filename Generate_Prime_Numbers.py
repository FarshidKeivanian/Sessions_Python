#!/usr/bin/env python
# coding: utf-8

# In[2]:


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    """Generate an infinite sequence of prime numbers."""
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# Example of using the generator
prime_generator = generate_primes()
for i in range(10):  # Generate the first 10 primes for demonstration
    print(next(prime_generator))


# In[ ]:




