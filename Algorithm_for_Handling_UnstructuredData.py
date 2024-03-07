#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')  # Download the Punkt tokenizer models
nltk.download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis

# Sample unstructured data: Social media post
post = "I love this new smartphone. It has amazing features!"

# Tokenizing the text
tokens = word_tokenize(post)
print(f'Tokens: {tokens}')

# Performing sentiment analysis
sia = SentimentIntensityAnalyzer()
sentiment_score = sia.polarity_scores(post)
print(f'Sentiment Score: {sentiment_score}')


# In[ ]:




