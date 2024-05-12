def count_words(text):
    # تقسیم متن به کلمات بر اساس فضای خالی
    words = text.split()
    # برگرداندن تعداد کلمات
    return len(words)

# نمونه متن ورودی
input_text = "سلام، چطور هستید؟ امیدوارم حالتان خوب باشد."
# فراخوانی تابع و چاپ تعداد کلمات
print("تعداد کلمات:", count_words(input_text))
