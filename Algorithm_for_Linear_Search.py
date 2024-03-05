#!/usr/bin/env python
# coding: utf-8

# In[1]:


def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

# Example usage
items = [5, 3, 7, 1, 9]
target = 7
print(linear_search(items, target))  # Output: 2


# In[ ]:




