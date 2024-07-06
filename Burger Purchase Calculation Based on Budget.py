# Burger Purchase Problem
budget = 50
cost_per_burger = 8

# Calculate the number of burgers and remaining money
num_burgers = budget // cost_per_burger
remaining_money = budget % cost_per_burger

print(f"You can buy {num_burgers} burgers and you'll have ${remaining_money} left.")
