import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a function to compute the view direction based on pitch and yaw angles
def compute_view_direction(pitch, yaw):
    x = np.cos(np.radians(pitch)) * np.sin(np.radians(yaw))
    y = np.sin(np.radians(pitch))
    z = np.cos(np.radians(pitch)) * np.cos(np.radians(yaw))
    return x, y, z

# Generate a range of pitch and yaw angles
pitch_angles = np.linspace(-90, 90, num=20)  # from looking straight down to straight up
yaw_angles = np.linspace(-180, 180, num=36)  # full 360 degree rotation

# Prepare for 3D plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Calculate and plot the direction vector for each combination of pitch and yaw
for pitch in pitch_angles:
    for yaw in yaw_angles:
        x, y, z = compute_view_direction(pitch, yaw)
        ax.quiver(0, 0, 0, x, y, z, color='blue', length=0.1, normalize=True)

# Setting the plot limits and labels
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Camera View Direction for Varying Pitch and Yaw Angles')

# Show the plot
plt.show()
