import matplotlib.pyplot as plt
import numpy as np

initial_x = 0.0
initial_y = 0.0
initial_velocity = 50.0
launch_angle = 45

angle_rad = np.radians(launch_angle)

gravity = 9.81

initial_horizontal_velocity = initial_velocity * np.cos(angle_rad)
initial_vertical_velocity = initial_velocity * np.sin(angle_rad)

time = 0
time_step = 0.01

x_values = []
y_values = []

while True:
    x = initial_x + initial_horizontal_velocity * time
    y = initial_y + initial_vertical_velocity * time - 0.5 * gravity * time ** 2

    if y < 0:
        break

    x_values.append(x)
    y_values.append(y)
    time += time_step

# Create a figure with the correct colors for the Ukrainian flag
fig, ax = plt.subplots()
ax.plot(x_values, y_values, color='blue', label='Траєкторія снаряду', linestyle='-')
ax.set_xlabel('Відстань (м)')
ax.set_ylabel('Висота (м)')
ax.set_title('Траєкторія снаряду')
ax.grid()

# Add a yellow lower half for the Ukrainian flag
ax.fill_between(x_values, 0, y_values, where=[y >= min(y_values)/2 for y in y_values], color='#bdbbbb')

plt.show()