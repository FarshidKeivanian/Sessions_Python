#!/usr/bin/env python
# coding: utf-8

# In[4]:


def find_smallest_number(lst):
    # Check if the list is empty
    if not lst:
        return None  # Return None if the list is empty
    
    # Initialize the smallest number with the first element of the list
    smallest = lst[0]
    
    # Iterate through the list starting from the first element
    for number in lst:
        # Update the smallest number if a smaller number is found
        if number < smallest:
            smallest = number
            
    # Return the smallest number found
    return smallest

# Example usage
numbers = [34, 1, 78, 2, 65, 23]
print("The smallest number in the list is:", find_smallest_number(numbers))


# In[ ]:




