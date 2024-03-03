#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# لیستی از کلمات برای حدس زدن
words = ['apple', 'banana', 'cherry', 'date', 'grape', 'lemon', 'mango', 'orange', 'pear', 'watermelon']

# انتخاب تصادفی یک کلمه از لیست
secret_word = random.choice(words)
guessed_letters = []  # حروف حدس زده شده
tries = 7  # تعداد تلاش‌های مجاز

print("به بازی جلاد خوش آمدید!")

# حلقه اصلی بازی
while tries > 0:
    output = ''
    for letter in secret_word:
        if letter in guessed_letters:
            output += letter
        else:
            output += '_'
    if output == secret_word:
        break
    print("کلمه مخفی: ", output)
    print("تعداد تلاش‌های باقیمانده: ", tries)

    guess = input("یک حرف حدس بزنید: ").lower()
    if guess in guessed_letters:
        print("این حرف قبلا حدس زده شده است.")
        continue
    elif guess in secret_word:
        print("درست است!")
        guessed_letters.append(guess)
    else:
        print("نادرست. دوباره تلاش کنید.")
        tries -= 1
        guessed_letters.append(guess)

if tries:
    print("تبریک! شما کلمه را حدس زدید: ", secret_word)
else:
    print("متاسفم! تلاش‌ها به پایان رسید. کلمه مخفی بود: ", secret_word)

