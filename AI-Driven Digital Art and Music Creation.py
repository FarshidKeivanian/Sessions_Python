import openai
from PIL import Image
import requests
from io import BytesIO
import os
import librosa
import numpy as np
import soundfile as sf

# تنظیم کلید API برای استفاده از DALL·E
openai.api_key = os.getenv("OPENAI_API_KEY")  # مطمئن شوید که کلید API تنظیم شده است

# 1. تولید تصویر دیجیتال با DALL·E
def generate_image(prompt, output_file="output_image.png"):
    try:
        print("در حال تولید تصویر...")
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response["data"][0]["url"]

        # دانلود و ذخیره تصویر
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image.save(output_file)
        print(f"تصویر تولید شده ذخیره شد: {output_file}")
        return output_file
    except Exception as e:
        print(f"خطا در تولید تصویر: {e}")
        return None

# 2. تولید موسیقی با الگوریتم ساده
def generate_music(output_file="output_music.wav", duration=10, sample_rate=44100):
    print("در حال تولید موسیقی...")
    # ایجاد موج سینوسی ساده (صدای سینتی‌سایزر)
    t = np.linspace(0, duration, int(sample_rate * duration))
    frequency = 440.0  # فرکانس A4
    audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)

    # ذخیره موسیقی به فایل
    sf.write(output_file, audio_data, sample_rate)
    print(f"موسیقی تولید شده ذخیره شد: {output_file}")
    return output_file

# 3. ویرایش تصویر (افزودن افکت هنری)
def add_artistic_filter(input_file, output_file="filtered_image.png"):
    try:
        print("در حال افزودن افکت هنری به تصویر...")
        image = Image.open(input_file).convert("RGB")
        filtered_image = image.filter(Image.Filter.DETAIL)
        filtered_image.save(output_file)
        print(f"تصویر با افکت ذخیره شد: {output_file}")
        return output_file
    except Exception as e:
        print(f"خطا در افزودن افکت: {e}")
        return None

# برنامه اصلی
if __name__ == "__main__":
    # تولید تصویر با DALL·E
    prompt = "A futuristic cityscape with glowing lights and advanced technology"
    image_file = generate_image(prompt)

    # افزودن افکت هنری به تصویر تولید شده
    if image_file:
        add_artistic_filter(image_file)

    # تولید موسیقی دیجیتال
    generate_music(duration=15)
