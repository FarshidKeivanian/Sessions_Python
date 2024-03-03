#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
from tkinter import messagebox

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("بازی جلاد")
        self.geometry("400x300")
        
        # کلمه مورد نظر برای حدس زدن
        self.secret_word = "Farshid"
        self.guessed_letters = ["_"] * len(self.secret_word)
        self.attempts = 6

        self.create_widgets()

    def create_widgets(self):
        # نمایش کلمه حدس زده شده
        self.label_word = tk.Label(self, text=" ".join(self.guessed_letters))
        self.label_word.pack(pady=20)

        # ورودی برای حرف
        self.entry_letter = tk.Entry(self)
        self.entry_letter.pack(pady=5)

        # دکمه برای حدس حرف
        guess_button = tk.Button(self, text="حدس بزن", command=self.guess_letter)
        guess_button.pack(pady=5)

        # نمایش تلاش‌های باقی‌مانده
        self.label_attempts = tk.Label(self, text=f"تلاش‌های باقی‌مانده: {self.attempts}")
        self.label_attempts.pack(pady=10)

    def guess_letter(self):
        letter = self.entry_letter.get()
        self.entry_letter.delete(0, tk.END)  # پاک کردن ورودی

        if letter in self.secret_word:
            for index, char in enumerate(self.secret_word):
                if char == letter:
                    self.guessed_letters[index] = letter
            self.label_word.config(text=" ".join(self.guessed_letters))
        else:
            self.attempts -= 1
            self.label_attempts.config(text=f"تلاش‌های باقی‌مانده: {self.attempts}")

        if "_" not in self.guessed_letters or self.attempts <= 0:
            self.end_game()

    def end_game(self):
        if "_" not in self.guessed_letters:
            messagebox.showinfo("پایان بازی", "تبریک! شما برنده شدید!")
        else:
            messagebox.showinfo("پایان بازی", f"متاسفانه شما باختید! کلمه '{self.secret_word}' بود.")
        self.destroy()

if __name__ == "__main__":
    app = HangmanGame()
    app.mainloop()

