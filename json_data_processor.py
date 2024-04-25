import json

# تابعی برای خواندن داده‌ها از فایل JSON
def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# استفاده از راو استرینگ برای جلوگیری از مشکلات مسیر فایل
data = read_json_file(r'D:/headlines_2024-04-25.json')
print(data)

# بررسی و افزودن کلید به هر آیتم در لیست
for item in data:
    if 'key_to_check' in item:
        item['key_to_check'] = 'new_value'
    else:
        item['new_key'] = 'new_value'

# دوباره استفاده از راو استرینگ برای مسیر ذخیره‌سازی فایل
write_json_file(data, r'D:/modified_headlines_2024-04-25.json')
