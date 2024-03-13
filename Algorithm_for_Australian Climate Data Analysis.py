# Sample temperature data for Australian cities
temperature_data = {
    "Sydney": [25, 26, 28, 22],
    "Melbourne": [19, 20, 15, 14],
    "Brisbane": [30, 31, 29, 26]
}

# Calculate the average temperature for each city
for city, temperatures in temperature_data.items():
    average_temp = sum(temperatures) / len(temperatures)
    print(f"Average temperature in {city}: {average_temp:.2f}°C")
