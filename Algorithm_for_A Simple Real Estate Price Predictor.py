#!/usr/bin/env python
# coding: utf-8

# In[10]:


def predict_price(square_feet, slope, intercept):
    """Predicts the price based on square footage using a simple linear model."""
    return slope * square_feet + intercept

# Example model coefficients (slope and intercept) - these would be determined by your model in a real scenario.
slope = 300  # Example slope
intercept = 10000  # Example intercept

def main():
    try:
        # Ask the user to input the square footage.
        square_feet = float(input("Enter the square footage: "))
        
        # Call the predict_price function with the user input and model coefficients.
        price = predict_price(square_feet, slope, intercept)
        
        # Print the predicted price.
        print(f"The predicted price is: ${price:.2f}")
    except ValueError:
        print("Please enter a valid number for square footage.")

if __name__ == "__main__":
    main()


# In[ ]:




