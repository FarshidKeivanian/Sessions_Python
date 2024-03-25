import matplotlib.pyplot as plt
import numpy as np

# Define the range for x values
x_values = np.linspace(-10, 10, 400)

# Function E: Linear function through the origin with positive slope
slope_E = 2  # positive slope
function_E = slope_E * x_values  # linear function f(x) = 2x

# Function F: Parabola that opens downward with vertex at (0,1)
a_F = -1  # negative coefficient since the parabola opens downward
vertex_F = (0, 1)
function_F = a_F * (x_values - vertex_F[0])**2 + vertex_F[1]  # f(x) = -x^2 + 1

# Function G: Step function
function_G = np.floor(x_values)  # step function, increasing in steps of 1

# Function H: Exponential decay function
a_H = 3  # coefficient when x=0, f(x)=3
b_H = 0.5  # base of the exponential decay
function_H = a_H * b_H**x_values  # f(x) = 3 * (1/2)^x

# Create the figure and the axes
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot Function E
axs[0, 0].plot(x_values, function_E, label='f(x) = 2x')
axs[0, 0].set_title('Function E: Linear')
axs[0, 0].axhline(0, color='black', linewidth=0.5)
axs[0, 0].axvline(0, color='black', linewidth=0.5)
axs[0, 0].grid(True)
axs[0, 0].legend()

# Plot Function F
axs[0, 1].plot(x_values, function_F, label='f(x) = -x^2 + 1')
axs[0, 1].set_title('Function F: Quadratic')
axs[0, 1].axhline(0, color='black', linewidth=0.5)
axs[0, 1].axvline(0, color='black', linewidth=0.5)
axs[0, 1].grid(True)
axs[0, 1].legend()

# Plot Function G
axs[1, 0].step(x_values, function_G, label='Step Function')
axs[1, 0].set_title('Function G: Step Function')
axs[1, 0].axhline(0, color='black', linewidth=0.5)
axs[1, 0].axvline(0, color='black', linewidth=0.5)
axs[1, 0].grid(True)
axs[1, 0].legend()

# Plot Function H
axs[1, 1].plot(x_values, function_H, label='f(x) = 3 * (1/2)^x')
axs[1, 1].set_title('Function H: Exponential Decay')
axs[1, 1].axhline(0, color='black',linewidth=0.5)
axs[1, 1].axvline(0, color='black',linewidth=0.5)
axs[1, 1].grid(True)
axs[1, 1].legend()

#Adjust the layout
plt.tight_layout()
plt.show()