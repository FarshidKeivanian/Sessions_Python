#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
def is_prime(number):
    if number < 2:
        return "Not Prime"
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"

# Example usage
number = 29
print(f"{number} is {is_prime(number)}")


# In[ ]:




