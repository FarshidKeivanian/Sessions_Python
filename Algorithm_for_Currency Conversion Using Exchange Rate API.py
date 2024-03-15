import requests

# Getting user input
currency_from = input("Please enter the base currency: ")
currency_to = input("Please enter the target currency: ")
amount = float(input("Enter the amount of money you want to convert: "))

# Constructing the URL for API request
url = f"https://api.exchangerate-api.com/v4/latest/{currency_from}"

# Sending the request and getting the response
response = requests.get(url)
data = response.json()

# Calculating the conversion rate and the converted amount
rate = data['rates'][currency_to]
converted_amount = amount * rate

# Displaying the result
print(f"{amount} {currency_from} is equivalent to {converted_amount} {currency_to}.")