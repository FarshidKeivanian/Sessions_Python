import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define vertices of a unit cube centered at origin in object space
object_cube_vertices = np.array([
    [-0.5, -0.5, -0.5],
    [0.5, -0.5, -0.5],
    [0.5,  0.5, -0.5],
    [-0.5,  0.5, -0.5],
    [-0.5, -0.5,  0.5],
    [0.5, -0.5,  0.5],
    [0.5,  0.5,  0.5],
    [-0.5,  0.5,  0.5]
])

# Define faces of the cube
faces = [[object_cube_vertices[j] for j in [0, 1, 2, 3]],
         [object_cube_vertices[j] for j in [4, 5, 6, 7]], 
         [object_cube_vertices[j] for j in [0, 1, 5, 4]], 
         [object_cube_vertices[j] for j in [2, 3, 7, 6]], 
         [object_cube_vertices[j] for j in [1, 2, 6, 5]],
         [object_cube_vertices[j] for j in [4, 7, 3, 0]]]

# Transformation vector
translation_vector = np.array([5, 10, -3])

# Apply transformation to the cube vertices to get world space vertices
world_cube_vertices = object_cube_vertices + translation_vector

# Define faces of the transformed cube
transformed_faces = [[world_cube_vertices[j] for j in [0, 1, 2, 3]],
                     [world_cube_vertices[j] for j in [4, 5, 6, 7]], 
                     [world_cube_vertices[j] for j in [0, 1, 5, 4]], 
                     [world_cube_vertices[j] for j in [2, 3, 7, 6]], 
                     [world_cube_vertices[j] for j in [1, 2, 6, 5]],
                     [world_cube_vertices[j] for j in [4, 7, 3, 0]]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot object space cube
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
# Plot world space cube
ax.add_collection3d(Poly3DCollection(transformed_faces, facecolors='magenta', linewidths=1, edgecolors='r', alpha=.25))

# Set plot limits
ax.set_xlim([-1, 6])
ax.set_ylim([-1, 11])
ax.set_zlim([-4, 2])

# Labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Title
plt.title('Cube Transformation from Object Space to World Space')

plt.show()
