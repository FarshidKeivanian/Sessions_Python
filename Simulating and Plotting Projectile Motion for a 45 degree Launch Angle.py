import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, angle, time):
    g = 9.81  # Acceleration due to gravity (m/s^2)
    angle_rad = np.radians(angle)
    
    # Horizontal and vertical components of initial velocity
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)
    
    # Position as a function of time
    x = v0x * time
    y = v0y * time - 0.5 * g * time**2
    
    return x, y

# Initial conditions
v0 = 50  # Initial velocity (m/s)
angle = 45  # Launch angle (degrees)

# Calculate time of flight (the time it takes for the projectile to land)
t_flight = 2 * v0 * np.sin(np.radians(angle)) / g

# Generate time points up to the calculated time of flight
t = np.linspace(0, t_flight, num=100)

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
