import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Using fetch_20newsgroups dataset as a placeholder
from sklearn.datasets import fetch_20newsgroups

# Load dataset
categories = ['alt.atheism', 'soc.religion.christian']
data = fetch_20newsgroups(subset='all', categories=categories, shuffle=True, random_state=42)

# Extract features using TF-IDF Vectorizer
tfidf_vect = TfidfVectorizer(stop_words='english')
X_tfidf = tfidf_vect.fit_transform(data.data)

# Labels
y = data.target

# Split dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.25, random_state=42)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)

# Confusion Matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# Performance metrics
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Predicting new emails (example)
new_emails = ["Free lottery tickets", "Weekly meeting agenda"]
new_emails_counts = tfidf_vect.transform(new_emails)
predictions = clf.predict(new_emails_counts)
print("Predictions:", predictions)  # Output: array of 0s and 1s indicating not spam or spam
