import numpy as np
import matplotlib.pyplot as plt

# Define the circle centers and radii
center1 = (0, 0)
radius1 = 5
center2 = (3, 4)
radius2 = 3

# Calculate the distance between the centers
distance = np.sqrt((center2[0] - center1[0])**2 + (center2[1] - center1[1])**2)

# Calculate 'a' - the distance from the center of the first circle to the line joining the points of intersection
a = (radius1**2 - radius2**2 + distance**2) / (2 * distance)

# Calculate the height 'h' of the triangle formed by the intersection points and the centers
h = np.sqrt(radius1**2 - a**2)

# Calculate the point P where the line through the intersections crosses the line between the centers
Px = center1[0] + a * (center2[0] - center1[0]) / distance
Py = center1[1] + a * (center2[1] - center1[1]) / distance
P = (Px, Py)

# Calculate the intersection points
intersection1 = (Px + h * (center2[1] - center1[1]) / distance, Py - h * (center2[0] - center1[0]) / distance)
intersection2 = (Px - h * (center2[1] - center1[1]) / distance, Py + h * (center2[0] - center1[0]) / distance)

# Plot the circles and the intersection points
theta = np.linspace(0, 2 * np.pi, 100)

circle1_x = center1[0] + radius1 * np.cos(theta)
circle1_y = center1[1] + radius1 * np.sin(theta)

circle2_x = center2[0] + radius2 * np.cos(theta)
circle2_y = center2[1] + radius2 * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(circle1_x, circle1_y, label='Circle 1')
plt.plot(circle2_x, circle2_y, label='Circle 2')
plt.scatter(*intersection1, color='red', zorder=5)
plt.scatter(*intersection2, color='red', zorder=5)
plt.scatter(*center1, color='blue', zorder=5)
plt.scatter(*center2, color='blue', zorder=5)

# Annotate the intersection points
plt.annotate(f'Intersection 1\n{intersection1}', xy=intersection1, xytext=(intersection1[0]+0.5, intersection1[1]),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(f'Intersection 2\n{intersection2}', xy=intersection2, xytext=(intersection2[0]-2, intersection2[1]-2),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Intersection of Two Circles')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Show the plot
plt.show()
