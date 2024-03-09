import requests
from datetime import datetime

def convert_unix_to_datetime(unix_time):
    try:
        datetime_obj = datetime.utcfromtimestamp(unix_time)
        formatted_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time
    except Exception as e:
        print(f"Error converting Unix timestamp: {e}")
        return "N/A"

def get_weather_forecast(city_name, units, days=5):
    api_key = "74322c58f63ab96a7550f46e411a427d"
    if units.lower() == 'celsius':
        unit_parameter = 'metric'
    elif units.lower() == 'fahrenheit':
        unit_parameter = 'imperial'
    else:
        print("Invalid unit. Please choose either Celsius or Fahrenheit.")
        return
    
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units={unit_parameter}"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if "list" in data:
        forecast_data = data["list"][:days*8]  # Get forecast data for the specified number of days (5 days * 8 forecasts per day)
        
        print(f"Weather forecast in {city_name} for the next {days} days:")
        for forecast in forecast_data:
            forecast_time = convert_unix_to_datetime(forecast["dt"])
            temperature = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            description = forecast["weather"][0]["description"]
            wind_speed = forecast["wind"]["speed"]
            print(f"Forecast time: {forecast_time}")
            print(f"Temperature: {temperature}°C" if unit_parameter == "metric" else f"Temperature: {temperature}°F")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description}")
            print(f"Wind Speed: {wind_speed} m/s")
            print("")

    else:
        print("City not found or no forecast data available!")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    units = input("Choose temperature unit (Celsius/Fahrenheit): ")
    days = int(input("Enter the number of days for forecast (default is 5): ") or "5")
    get_weather_forecast(city_name, units, days)
