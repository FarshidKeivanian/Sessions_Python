import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# Define the plotting function
def plot_function(ax, function, x_range):
    x = np.linspace(*x_range, 400)
    y = eval(function)
    ax.clear()  # Clear previous plots
    ax.plot(x, y)
    plt.draw()

# Initialize plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_title('Graphing Calculator')

# Text box for function input
text_box_ax = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(text_box_ax, 'Enter Function (e.g., x**2): ')

# Specify the range for x values
x_range = [-10, 10]  # Example range from -10 to 10

# Callback function to update plot
def submit(expression):
    function = expression.replace('^', '**')
    plot_function(ax, function, x_range)

text_box.on_submit(submit)

plt.show()