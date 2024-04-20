import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, angle, time):
    g = 9.81  # acceleration due to gravity (m/s^2)
    angle_rad = np.radians(angle)
    
    # Horizontal and vertical components of initial velocity
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)
    
    # Position as a function of time
    x = v0x * time
    y = v0y * time - 0.5 * g * time**2
    
    return x, y

# Initial conditions
v0 = 50  # initial velocity (m/s)
angle = 45  # launch angle (degrees)

# Generate time points
t = np.linspace(0, 10, num=100)

# Calculate trajectory
trajectory = np.array([projectile_motion(v0, angle, ti) for ti in t])

# Plotting the trajectory
plt.figure()
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.title('Projectile Motion at 45°')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.show()
