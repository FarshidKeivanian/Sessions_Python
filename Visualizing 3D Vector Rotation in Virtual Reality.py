import numpy as np  # Import numpy
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

# Original vector representing a point in VR space
original_vector = np.array([2, 2, 0])

# Rotation transformation: user looks up by 45 degrees
rotation_degrees = 45
rotation_radians = np.radians(rotation_degrees)
rotation = R.from_euler('x', rotation_radians)

# Apply rotation to the original vector
rotated_vector = rotation.apply(original_vector)

# Plotting the original and transformed vector in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, *original_vector, color='blue', label='Original')
ax.quiver(0, 0, 0, *rotated_vector, color='green', label='Rotated')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('VR Rendering: Geometric Transformation')
plt.legend()
plt.show()
