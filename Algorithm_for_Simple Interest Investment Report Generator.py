def calculate_interest(starting_balance, rate):
    # Calculate the interest for one year
    interest = starting_balance * (rate / 100)
    return interest

def generate_report(investment, years, rate):
    starting_balance = investment
    total_interest = 0

    # Header for the report table
    print(f"{'Year':<5} {'Starting Balance':<20} {'Interest':<15} {'Ending Balance'}")
    
    # Iterate over each year to calculate and display the report
    for year in range(1, years + 1):
        interest = calculate_interest(starting_balance, rate)
        ending_balance = starting_balance + interest
        print(f"{year:<5} {starting_balance:<20.1f} {interest:<15.1f} {ending_balance:.1f}")
        starting_balance = ending_balance  # Update for next year
        total_interest += interest
    
    # Print the totals after the loop
    print(f"\nEnding Balance: {starting_balance:.3f}")
    print(f"Total Interest Earned: {total_interest:.3f}")

# Taking inputs from the user
investment = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years(as 1 or 2 or 3... or 10): "))
rate = float(input("Enter the rate as (Ex: 0.1, 5.5, 9.8 etc)%: "))

# Generating the report
generate_report(investment, years, rate)
