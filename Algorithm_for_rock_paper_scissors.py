#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def rock_paper_scissors():
    choices = ["سنگ", "کاغذ", "قیچی"]
    while True:
        user_input = input("انتخاب کنید (سنگ، کاغذ، قیچی) یا 'خروج' برای پایان: ")
        if user_input == "خروج":
            print("بازی به پایان رسید.")
            break
        if user_input not in choices:
            print("انتخاب نامعتبر است. لطفا دوباره امتحان کنید.")
            continue

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




