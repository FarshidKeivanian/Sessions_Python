# Define a dictionary with days of the week as keys and corresponding moods as values
week_moods = {
    "Monday": "Motivated",
    "Tuesday": "Productive",
    "Wednesday": "Energetic",
    "Thursday": "Thoughtful",
    "Friday": "Joyful",
    "Saturday": "Relaxed",
    "Sunday": "Peaceful"
}

# Ask the user to input a day of the week
user_day = input("Enter a day of the week to know the mood: ").capitalize()

# Check if the entered day is in the dictionary and respond accordingly
if user_day in week_moods:
    print(f"The mood for {user_day} is: {week_moods[user_day]}")
else:
    print("Please enter a valid day of the week.")
