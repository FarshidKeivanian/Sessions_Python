from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
# Step 1: Collect and label data
# Using `fetch_20newsgroups` as a placeholder for email data
categories = ['alt.atheism', 'soc.religion.christian']
data = fetch_20newsgroups(subset='all', categories=categories, shuffle=True, random_state=42)
# Step 2: Extract features
# Convert text to a matrix of TF-IDF features
tfidf_vect = TfidfVectorizer(stop_words='english')
X_tfidf = tfidf_vect.fit_transform(data.data)
# Labels
y = data.target
# Step 3: Split dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.25, random_state=42)
# Step 4: Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, y_train)
# Step 5: Evaluate the model
y_pred = clf.predict(X_test)
# Confusion Matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# Performance metrics
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
# Refine the model and predict on new emails
# This is an iterative process. Based on the evaluation, you may choose to adjust your model,
# perhaps by tuning parameters, or using a different set of features.
print(data)