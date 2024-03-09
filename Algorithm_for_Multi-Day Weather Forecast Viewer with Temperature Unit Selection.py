#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

def get_weather(city_name):
    api_key = "74322c58f63ab96a7550f46e411a427d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main_info = data["main"]
        weather_info = data["weather"][0]
        temperature = main_info["temp"]
        humidity = main_info["humidity"]
        description = weather_info["description"]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City not found!")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    get_weather(city_name)


# In[ ]:





# In[ ]:





# In[5]:


import requests
from datetime import datetime

API_KEY = '74322c58f63ab96a7550f46e411a427d'  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def convert_unix_to_readable(unix_time):
    """Converts Unix timestamp to readable format."""
    return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')

def get_weather(city):
    complete_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data.get('cod') != 200:
        print("Failed to fetch weather data")
        return

    wind_speed = weather_data['wind']['speed']
    sunrise_time = convert_unix_to_readable(weather_data['sys']['sunrise'])
    sunset_time = convert_unix_to_readable(weather_data['sys']['sunset'])
    pressure = weather_data['main']['pressure']

    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Sunrise Time: {sunrise_time}")
    print(f"Sunset Time: {sunset_time}")
    print(f"Atmospheric Pressure: {pressure} hPa")

def get_forecast(city, days):
    complete_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data.get('cod') != 200:
        print("Failed to fetch location data")
        return

    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']
    
    one_call_url = f"{BASE_URL}onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,current,alerts&appid={API_KEY}&units=metric"
    response = requests.get(one_call_url)
    forecast_data = response.json()

    if 'daily' not in forecast_data:
        print("Failed to fetch forecast data")
        return

    for day in forecast_data['daily'][:days]:
        date = convert_unix_to_readable(day['dt'])
        day_temp = day['temp']['day']
        weather_description = day['weather'][0]['description']
        print(f"Date: {date}, Temperature: {day_temp}°C, Weather: {weather_description}")

# Example usage
city_name = "Tehran"  # Replace with the desired city name
get_weather(city_name)
get_forecast(city_name, 3)  # Forecast for 3 days


# In[11]:


import requests

def get_coordinates(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        latitude = data["coord"]["lat"]
        longitude = data["coord"]["lon"]
        return latitude, longitude
    else:
        print("City not found!")
        return None, None

def get_forecast(latitude, longitude, api_key, days=3):
    base_url = "http://api.openweathermap.org/data/2.5/onecall?"
    exclude = "minutely,hourly,alerts,current"
    complete_url = f"{base_url}lat={latitude}&lon={longitude}&exclude={exclude}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if "daily" in data:
        print(f"Weather forecast for the next {days} days:")
        for i in range(days):
            day = data["daily"][i]
            date = datetime.utcfromtimestamp(day["dt"]).strftime('%Y-%m-%d')
            temp_day = day["temp"]["day"]
            description = day["weather"][0]["description"]
            print(f"Date: {date}, Temperature: {temp_day}°C, Description: {description}")
    else:
        print("Forecast data not found!")

if __name__ == "__main__":
    api_key = "74322c58f63ab96a7550f46e411a427d"
    city_name = input("Enter the city name: ")
    latitude, longitude = get_coordinates(city_name, api_key)
    if latitude is not None and longitude is not None:
        days = int(input("Enter the number of days for the forecast (3, 5, or 7): "))
        get_forecast(latitude, longitude, api_key, days)


# In[13]:


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


# In[ ]:




