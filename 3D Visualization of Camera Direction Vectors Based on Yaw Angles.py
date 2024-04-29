import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the target position vector for the robotic arm's end effector
target_vector = np.array([3, 2, 5])

# Create a 3D plot to visualize the robotic arm's reach
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the vector from the origin to the target point
ax.quiver(0, 0, 0, *target_vector, length=np.linalg.norm(target_vector), color='red')

# Set the limits for the axes
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])

# Labeling the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Title of the plot
plt.title('3D Visualization of Robotic Arm Reach to Target Position')

# Display the plot
plt.show()
