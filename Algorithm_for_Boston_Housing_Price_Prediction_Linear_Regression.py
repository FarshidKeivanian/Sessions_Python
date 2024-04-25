# وارد کردن کتابخانه‌های لازم
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# بارگذاری دیتاست از فایل CSV
data = pd.read_csv('D:/boston_house_prices_corrected.csv')

# تفکیک داده‌ها به ویژگی‌ها و هدف
# فرض بر این است که ستون آخر، مقدار هدف (قیمت) است
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# تقسیم دیتاست به دو بخش: آموزشی و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل رگرسیون خطی
lr = LinearRegression()

# آموزش مدل بر روی داده‌های آموزشی
lr.fit(X_train, y_train)

# پیش‌بینی بر روی داده‌های تست
y_pred = lr.predict(X_test)

# محاسبه خطای مربع میانگین
mse = mean_squared_error(y_test, y_pred)
print(f'خطای مربع میانگین: {mse:.2f}')
