#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np

# Define the square function
def square(x):
    return x * x

# Generate a range of x values
x_values = np.linspace(-10, 10, 400) # 400 points from -10 to 10

# Apply the square function to each x value
y_values = square(x_values)

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = x^2')
plt.title('Plot of the function f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()


# In[ ]:




