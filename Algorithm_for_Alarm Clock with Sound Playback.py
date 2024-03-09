#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# You may need to install pygame first
# pip install pygame
# pip install pygame
import datetime
import time
import pygame  # Import pygame for playing sounds

def set_alarm():
    alarm_time = input("Please enter the alarm time in HH:MM:SS format (for 24-hour format) or HH:MM:SS AM/PM format (for 12-hour format), e.g., 07:30:00 PM: ")

    try:
        alarm_time_object = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        try:
            alarm_time_object = datetime.datetime.strptime(alarm_time, "%I:%M:%S %p")
        except ValueError:
            print("Invalid time format. Please try again.")
            return
    
    now = datetime.datetime.now()
    alarm_time_object = alarm_time_object.replace(year=now.year, month=now.month, day=now.day)
    
    print(f"Current time: {now.strftime('%I:%M:%S %p')}")
    print(f"Alarm set for: {alarm_time_object.strftime('%I:%M:%S %p')}")
    
    while True:
        now = datetime.datetime.now()
        if now >= alarm_time_object:
            print("ALARM ALARM ALARM! It's time to wake up!")            
            # Initialize pygame mixer
            pygame.mixer.init()
            # Load the sound file
            pygame.mixer.music.load('C:/alarm1.mp3') #alarm1/alarm2/alarm3 at https://github.com/FarshidKeivanian/Sessions_Python_R
            # Play the sound
            pygame.mixer.music.play()            
            # Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)            
            break  # Exit the loop after playing the sound
        time.sleep(1)

set_alarm()

