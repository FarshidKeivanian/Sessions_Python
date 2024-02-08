#!/usr/bin/env python
# coding: utf-8

# In[3]:


def find_largest_number(numbers):
    if not numbers:  # Check if the list is empty
        return None  # Return None if the list is empty
    largest = numbers[0]  # Initialize largest to the first number in the list
    for number in numbers[1:]:  # Start loop from the second element
        if number > largest:
            largest = number
    return largest

# Example usage of the function with a list of numbers
result = find_largest_number([3, 67, 99, 23, 45])
print(result)

