import matplotlib.pyplot as plt

coordinates = []
for i in range(5):  # outer loop
    for j in range(5):  # inner loop
        coordinates.append((i, j))


# Assuming 'coordinates' is populated as per the nested loop data generation
x, y = zip(*coordinates)
plt.scatter(x, y, marker='o')
plt.title('Visualization of Nested Loop Operations')
plt.xlabel('Outer Loop')
plt.ylabel('Inner Loop')
plt.grid(True)
plt.show()
