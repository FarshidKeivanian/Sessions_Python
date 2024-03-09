#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def analyze_user_choices(user_choices):
    # تجزیه و تحلیل انتخاب‌های قبلی کاربر برای پیدا کردن الگوها
    if len(user_choices) < 3:
        return random.choice(["سنگ", "کاغذ", "قیچی"])
    else:
        # اینجا می‌توان الگوریتم پیچیده‌تری برای تجزیه و تحلیل الگوها و انتخاب بهترین حدس اضافه کرد
        return random.choice(["سنگ", "کاغذ", "قیچی"])

def rock_paper_scissors():
    choices = ["سنگ", "کاغذ", "قیچی"]
    user_choices = []
    difficulty = input("لطفا سطح دشواری را انتخاب کنید (آسان، متوسط، دشوار): ")
    
    while True:
        user_input = input("انتخاب کنید (سنگ، کاغذ، قیچی) یا 'خروج' برای پایان: ")
        if user_input == "خروج":
            print("بازی به پایان رسید.")
            break
        if user_input not in choices:
            print("انتخاب نامعتبر است. لطفا دوباره امتحان کنید.")
            continue

        user_choices.append(user_input)

        if difficulty == "دشوار":
            computer_choice = analyze_user_choices(user_choices)
        else:
            computer_choice = random.choice(choices)
        
        print(f"انتخاب کامپیوتر: {computer_choice}")

        if user_input == computer_choice:
            print("مساوی شد!")
        elif (user_input == "سنگ" and computer_choice == "قیچی") or              (user_input == "کاغذ" and computer_choice == "سنگ") or              (user_input == "قیچی" and computer_choice == "کاغذ"):
            print("شما برنده شدید!")
        else:
            print("کامپیوتر برنده شد!")

rock_paper_scissors()


# In[ ]:




