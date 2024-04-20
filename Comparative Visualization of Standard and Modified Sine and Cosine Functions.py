import numpy as np
import matplotlib.pyplot as plt

# Constants
pi = np.pi

# Create a range of values from 0 to 2π
x = np.linspace(0, 2 * pi, 1000)

# Standard sine and cosine functions
y_sin = np.sin(x)
y_cos = np.cos(x)

# Modified sine and cosine functions for amplitude, period, and phase shift
amplitude = 2
period = pi  # period is π, so the function repeats every π instead of 2π
phase_shift = pi / 2  # phase shift by π/2 to the right

y_sin_mod = amplitude * np.sin(2 * pi * x / period + phase_shift)
y_cos_mod = amplitude * np.cos(2 * pi * x / period + phase_shift)

# Plotting
plt.figure(figsize=(12, 6))

# Plot standard sine and cosine
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.title('Standard Sine and Cosine Functions')

# Plot modified sine and cosine
plt.plot(x, y_sin_mod, label='2 * sin(2πx/π + π/2)', linestyle='--')
plt.plot(x, y_cos_mod, label='2 * cos(2πx/π + π/2)', linestyle='--')

plt.xlabel('x (radians)')
plt.ylabel('Function Value')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()

plt.show()
