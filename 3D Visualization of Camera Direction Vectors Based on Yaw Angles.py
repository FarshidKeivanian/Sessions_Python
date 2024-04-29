import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the target position vector for the robotic arm's end effector
target_vector = np.array([3, 2, 5])

# 3D plot for the robotic arm's reach
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, *target_vector, length=np.linalg.norm(target_vector), color='red')
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Robotic Arm End Effector Position')
plt.show()
