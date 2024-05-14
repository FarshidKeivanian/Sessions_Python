import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
# Attempt to load the dataset from the internet, otherwise create an artificial dataset.
try:
    url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
    df = pd.read_csv(url)
    print("Dataset loaded from URL")
except Exception as e:
    print("Error loading dataset from URL:", e)
    # Create an artificial dataset
    data = {
        'Survived': [0, 1, 1, 0, 1, 0, 0, 1, 1, 0] * 100,
        'Pclass': [3, 1, 3, 1, 3, 3, 2, 1, 2, 3] * 100,
        'Sex': ['male', 'female', 'female', 'male', 'female', 'male', 'male', 'female', 'female', 'male'] * 100,
        'Age': [22, 38, 26, 35, 28, 2, 58, 19, 24, 40] * 100,
        'SibSp': [1, 1, 0, 1, 0, 4, 0, 0, 0, 1] * 100,
        'Parch': [0, 0, 0, 0, 0, 2, 0, 0, 1, 0] * 100,
        'Fare': [7.25, 71.28, 7.92, 53.1, 8.05, 21.07, 26.55, 30.0, 10.5, 8.05] * 100,
        'Embarked': ['S', 'C', 'S', 'S', 'S', 'S', 'Q', 'C', 'S', 'S'] * 100
    }
    df = pd.DataFrame(data)
    print("Artificial dataset created")

# Print column names to verify 'Embarked' is present
print("Columns in DataFrame:", df.columns)

# Step 2: Data Preprocessing
# Convert textual values to numbers
if 'Sex' in df.columns:
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
else:
    print("Column 'Sex' not found in DataFrame")

if 'Embarked' in df.columns:
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
else:
    print("Column 'Embarked' not found in DataFrame")

# Fill missing values
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median(), inplace=True)
else:
    print("Column 'Age' not found in DataFrame")

if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
else:
    print("Column 'Embarked' not found in DataFrame")

# Split the data into features and labels
if 'Survived' in df.columns:
    X = df.drop(columns=['Survived'])
    y = df['Survived']
else:
    print("Column 'Survived' not found in DataFrame")

# Ensure all columns in X are numerical
if not all([pd.api.types.is_numeric_dtype(dtype) for dtype in X.dtypes]):
    print("Not all columns are numeric. Check data preprocessing steps.")
    # Convert all non-numeric columns to numeric if necessary
    for col in X.select_dtypes(include=['object']).columns:
        X[col] = pd.to_numeric(X[col], errors='coerce').fillna(0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 3: Build and Train Models
# Logistic Regression Model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_log_reg = log_reg.predict(X_test)

# Decision Tree Model
tree_clf = DecisionTreeClassifier()
tree_clf.fit(X_train, y_train)
y_pred_tree_clf = tree_clf.predict(X_test)

# Random Forest Model
forest_clf = RandomForestClassifier()
forest_clf.fit(X_train, y_train)
y_pred_forest_clf = forest_clf.predict(X_test)

# Step 4: Evaluate Models
# Evaluate Logistic Regression Model
print("Logistic Regression Accuracy: ", accuracy_score(y_test, y_pred_log_reg))
print("Classification Report: \n", classification_report(y_test, y_pred_log_reg))

# Evaluate Decision Tree Model
print("Decision Tree Accuracy: ", accuracy_score(y_test, y_pred_tree_clf))
print("Classification Report: \n", classification_report(y_test, y_pred_tree_clf))

# Evaluate Random Forest Model
print("Random Forest Accuracy: ", accuracy_score(y_test, y_pred_forest_clf))
print("Classification Report: \n", classification_report(y_test, y_pred_forest_clf))
