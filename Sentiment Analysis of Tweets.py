# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load the dataset directly from the provided link
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/tweets.csv"
tweets_df = pd.read_csv(url)

# Display the first few rows of the dataset to understand its structure
print("Sample tweets data:")
print(tweets_df.head())

# Function to classify sentiment based on polarity
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment analysis
tweets_df['Sentiment'] = tweets_df['tweet'].apply(get_sentiment)

# Display sentiment counts
sentiment_counts = tweets_df['Sentiment'].value_counts()
print("\nSentiment distribution:")
print(sentiment_counts)

# Plot the distribution of sentiments
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Sentiment Analysis of Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
