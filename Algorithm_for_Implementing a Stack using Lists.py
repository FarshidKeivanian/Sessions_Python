#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# Example usage
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.pop())  # Output: 10


# In[ ]:




