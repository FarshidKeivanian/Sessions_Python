#!/usr/bin/env python
# coding: utf-8

# In[1]:


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




