import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Step 1: Mock dataset
data = {
    'email': ['free viagra now', 'meeting schedule', 'cheap watches', 'project deadline', 'increase your income', 'happy birthday'],
    'label': [1, 0, 1, 0, 1, 0]  # 1: Spam, 0: Not Spam
}
df = pd.DataFrame(data)

# Step 2: Feature extraction (implicitly done here by creating a simple dataset)
# In practice, use techniques like TF-IDF or CountVectorizer on actual email content.

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(df['email'], df['label'], test_size=0.33, random_state=42)

# Convert text data into numerical data
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Step 3: Train Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# Step 4: Evaluate the model
y_pred = clf.predict(X_test_counts)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

# Step 5: Refinement and prediction on new emails
# Here, you might tune the model, use a different model, or preprocess the data differently based on the metrics.
# Predicting a new email
new_emails = ["free lottery tickets", "weekly meeting agenda"]
new_emails_counts = vectorizer.transform(new_emails)
predictions = clf.predict(new_emails_counts)
print("Predictions:", predictions)  # Output: array of 0s and 1s indicating not spam or spam
