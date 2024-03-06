#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Income Tax Calculator

def calculate_income_tax(gross_income, num_dependents):
    """
    Calculates income tax based on gross income and number of dependents.
    
    Parameters:
    - gross_income: float, the total gross income in dollars and cents
    - num_dependents: int, the number of dependents
    
    Returns:
    - tax: float, the calculated income tax with three decimal places
    """
    
    # Constants
    TAX_RATE = 0.25  # Flat tax rate of 25%
    STANDARD_DEDUCTION = 18500  # Standard deduction for taxpayer
    DEPENDENT_DEDUCTION = 1200  # Additional deduction per dependent
    
    # Calculate deductions
    total_deductions = STANDARD_DEDUCTION + (num_dependents * DEPENDENT_DEDUCTION)
    
    # Calculate taxable income
    taxable_income = max(0, gross_income - total_deductions)  # Ensuring taxable income is not negative
    
    # Calculate tax
    tax = taxable_income * TAX_RATE
    
    # Format tax to three decimal places
    tax = round(tax, 3)
    
    return tax

# User inputs
gross_income = float(input("Enter your gross income to the smallest penny: "))
num_dependents = int(input("Enter the number of dependents: "))

# Calculate income tax
income_tax = calculate_income_tax(gross_income, num_dependents)

# Display the result
print(f"Your income tax is: ${income_tax:.3f}")

