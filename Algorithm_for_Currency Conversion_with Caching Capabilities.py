import requests
import time

class CurrencyConverter:
    def __init__(self):
        self.cache = {}  # Cache to store exchange rates and their update times

    def get_exchange_rate(self, base_currency, target_currency):
        cache_key = f"{base_currency}_{target_currency}"
        current_time = time.time()

        # Check for the existence and validity of data in the cache
        if cache_key in self.cache and current_time - self.cache[cache_key]['time'] < 3600:  # Valid for 1 hour
            return self.cache[cache_key]['rate']

        # API request to get the exchange rate
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][target_currency]

        # Updating the cache
        self.cache[cache_key] = {'rate': rate, 'time': current_time}

        return rate

    def convert_currency(self, amount, base_currency, target_currency):
        rate = self.get_exchange_rate(base_currency, target_currency)
        return amount * rate

# Example of using the program
converter = CurrencyConverter()
base_currency = input("Enter the base currency: ")
target_currency = input("Enter the target currency: ")
amount = float(input("Enter the amount: "))

converted_amount = converter.convert_currency(amount, base_currency, target_currency)
print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")