import matplotlib.pyplot as plt
import numpy as np

# Initial and target positions
initial_position = np.array([1, 1])
target_position = np.array([8, 5])

# Movement vector
movement_vector = target_position - initial_position

# Plotting the unit movement
plt.quiver(*initial_position, *movement_vector, scale=1, scale_units='xy', angles='xy', color='blue')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('RTS Game Unit Movement Vector')
plt.show()
