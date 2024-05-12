def analyze_words(text):
    # تقسیم متن به کلمات و تبدیل آن به فرمت پایین
    words = text.lower().split()
    # ایجاد یک دیکشنری خالی برای نگهداری کلمات و تعداد تکرار
    word_count = {}
    # شمارش تعداد تکرار هر کلمه
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# نمونه متن ورودی
input_text = "سلام سلام چه خبر؟ چه خبر!"
# فراخوانی تابع و چاپ تجزیه و تحلیل کلمات
print("تجزیه و تحلیل کلمات:", analyze_words(input_text))
