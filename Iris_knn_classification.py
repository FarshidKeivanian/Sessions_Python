# وارد کردن کتابخانه‌های لازم
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# بارگذاری دیتاست
iris = load_iris()
X = iris.data
y = iris.target

# تقسیم دیتاست به دو بخش: آموزشی و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ایجاد مدل دسته‌بندی کِناره‌های نزدیکترین همسایه
knn = KNeighborsClassifier(n_neighbors=3)

# آموزش مدل بر روی داده‌های آموزشی
knn.fit(X_train, y_train)

# پیش‌بینی بر روی داده‌های تست
y_pred = knn.predict(X_test)

# محاسبه دقت مدل
accuracy = accuracy_score(y_test, y_pred)
print(f'دقت دسته‌بندی: {accuracy * 100:.2f}%')
