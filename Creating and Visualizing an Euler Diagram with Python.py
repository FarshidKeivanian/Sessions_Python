#pip install matplotlib-venn

# First, ensure that you have the matplotlib-venn package installed.
# You can install it using pip by running the following command in your terminal:
# pip install matplotlib-venn

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define the sets
set_a = {"Red", "Green", "Blue"}
set_b = {"Blue", "Yellow", "Orange"}

# Create the Euler Diagram
venn2([set_a, set_b], ('Set A', 'Set B'))

# Display the plot
plt.title("Euler Diagram Example")
plt.show()
