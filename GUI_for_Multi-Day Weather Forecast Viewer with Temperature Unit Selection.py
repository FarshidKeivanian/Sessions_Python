#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

def convert_unix_to_datetime(unix_time):
    try:
        datetime_obj = datetime.utcfromtimestamp(unix_time)
        formatted_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time
    except Exception as e:
        return "N/A"

def fetch_weather_forecast(city_name, units, days=5):
    api_key = "74322c58f63ab96a7550f46e411a427d"
    unit_parameter = 'metric' if units.lower() == 'celsius' else 'imperial'
    
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units={unit_parameter}"
    
    response = requests.get(complete_url)
    data = response.json()
    
    forecast_info = ""
    if "list" in data:
        forecast_data = data["list"][:days*8]
        
        for forecast in forecast_data:
            forecast_time = convert_unix_to_datetime(forecast["dt"])
            temperature = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            description = forecast["weather"][0]["description"]
            wind_speed = forecast["wind"]["speed"]
            forecast_info += f"زمان پیش‌بینی: {forecast_time}\nدما: {temperature}°{'C' if unit_parameter == 'metric' else 'F'}\nرطوبت: {humidity}%\nتوضیحات: {description}\nسرعت باد: {wind_speed} متر بر ثانیه\n\n"
    else:
        forecast_info = "شهر یافت نشد یا داده‌های پیش‌بینی موجود نیست!"
    return forecast_info

def get_weather_forecast_gui():
    root = tk.Tk()
    root.withdraw()  # Hides the main window
    
    city_name = simpledialog.askstring("ورودی", "نام شهر را وارد کنید:")
    units = simpledialog.askstring("ورودی", "واحد دما را انتخاب کنید (Celsius/Fahrenheit):")
    days = simpledialog.askinteger("ورودی", "تعداد روزهای پیش‌بینی را وارد کنید (پیش‌فرض 5 روز):", initialvalue=5)
    
    forecast_info = fetch_weather_forecast(city_name, units, days)
    messagebox.showinfo("پیش‌بینی آب و هوا", forecast_info)

if __name__ == "__main__":
    get_weather_forecast_gui()


# In[ ]:




