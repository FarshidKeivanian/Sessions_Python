def recursive_sum(N):
    # Base case: if N is 0 or 1, the sum up to N is simply N
    if N <= 1:
        return N
    # Recursive case: sum of N plus the sum of numbers up to N-1
    else:
        return N + recursive_sum(N-1)

# Example usage:
print(recursive_sum(10))  # Outputs: 55
