import requests

def get_conversion_rate(from_currency, to_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return rate

def convert_currencies():
    from_currency = input("Enter source currency unit: ").upper()
    to_currencies = input("Enter target currency units (separated by commas): ").upper().split(',')
    amount = float(input("Enter the amount of money: "))
    
    for to_currency in to_currencies:
        rate = get_conversion_rate(from_currency, to_currency.strip())
        converted_amount = amount * rate
        print(f"{amount} {from_currency} to {to_currency} = {converted_amount:.2f}")

convert_currencies()
