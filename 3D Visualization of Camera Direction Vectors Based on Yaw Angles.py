import numpy as np
import matplotlib.pyplot as plt

def camera_rotation(pitch, yaw):
    # Convert degrees to radians for computation
    pitch_rad = np.radians(pitch)
    yaw_rad = np.radians(yaw)
    
    # Calculate the direction vector
    x = np.cos(pitch_rad) * np.cos(yaw_rad)
    y = np.sin(pitch_rad)
    z = np.cos(pitch_rad) * np.sin(yaw_rad)
    
    return x, y, z

# Generate a range of yaw angles from -180 to 180 degrees
yaw_angles = np.linspace(-180, 180, 360)
pitch_angle = 30  # fixed pitch angle

# Calculate direction vectors
directions = np.array([camera_rotation(pitch_angle, yaw) for yaw in yaw_angles])

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, directions[:, 0], directions[:, 1], directions[:, 2], length=0.1)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Camera Directions at Pitch = 30°')
plt.show()
