import csv

# تابعی برای خواندن داده‌ها از یک فایل CSV
def read_csv_file(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# نمونه فایل CSV را می‌خوانیم و داده‌ها را چاپ می‌کنیم
data = read_csv_file('D:/bank.csv')
for row in data:
    print(row)
