# مقدمه بازی
print("به بازی ماجراجویی مبتنی بر متن خوش آمدید!")
print("شما در وسط یک جنگل ایستاده‌اید. دو مسیر پیش روی شماست: یکی به سمت چپ و دیگری به سمت راست.")

# گرفتن انتخاب کاربر
choice = input("آیا می‌خواهید به چپ بروید یا به راست؟ (چپ/راست) ")

# منطق شرطی برای پیگیری انتخاب کاربر
if choice == "چپ":
    print("شما به سمت چپ رفتید و به یک خانه قدیمی رسیدید. در خانه باز است.")
    # گرفتن انتخاب دوم کاربر
    choice2 = input("آیا می‌خواهید وارد خانه شوید؟ (بله/خیر) ")
    if choice2 == "بله":
        print("شما وارد خانه شدید و یک گنج پیدا کردید! شما برنده شدید!")
    else:
        print("شما تصمیم گرفتید که وارد خانه نشوید. ناگهان یک طوفان شروع شد و شما در بیرون گیر کردید. بازی تمام شد.")
elif choice == "راست":
    print("شما به سمت راست رفتید و با یک خرس برخورد کردید!")
    # گرفتن انتخاب دوم کاربر
    choice2 = input("آیا می‌خواهید با خرس بجنگید؟ (بله/خیر) ")
    if choice2 == "بله":
        print("متاسفانه خرس خیلی قوی بود و شما شکست خوردید. بازی تمام شد.")
    else:
        print("شما تصمیم گرفتید که فرار کنید و موفق شدید به امان برسید. اما ماجراجویی شما هنوز تمام نشده!")
else:
    print("انتخاب نامعتبر. لطفا فقط 'چپ' یا 'راست' را وارد کنید.")

# پایان بازی
print("متشکریم که بازی ما را امتحان کردید!")