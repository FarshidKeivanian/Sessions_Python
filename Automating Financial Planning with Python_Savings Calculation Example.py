# Python code to calculate the savings plan
def calculate_savings(goal_amount, weekly_savings):
    weeks_needed = goal_amount / weekly_savings
    return weeks_needed

# Example usage
goal_amount = 1200  # The cost of the laptop
weekly_savings = 100  # Amount saved per week

weeks_needed = calculate_savings(goal_amount, weekly_savings)
print(f'You need to save for {weeks_needed} weeks to reach your goal of ${goal_amount}.')
