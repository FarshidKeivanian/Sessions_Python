#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# Example usage
number = 5
print(f"Factorial of {number} is {factorial(number)}")


# In[ ]:




