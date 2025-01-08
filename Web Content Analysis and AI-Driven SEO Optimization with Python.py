import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

try:
    from transformers import pipeline
    transformers_installed = True
except ImportError:
    transformers_installed = False
    print("Transformers library is not installed. Skipping AI content generation.")

# 1. Collecting data from the website
url = "https://newcastle.edu.au/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title = soup.title.string if soup.title else "No title found"

    # Extract meta description with error handling
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    meta_desc = meta_tag['content'] if meta_tag and 'content' in meta_tag.attrs else "No meta description found"

    # Extract the page content
    content = soup.get_text()
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    title = "N/A"
    meta_desc = "N/A"
    content = ""

# 2. Analyzing website content
if content:
    nltk.download('stopwords')
    nltk.download('punkt')  # Required for tokenization
    stop_words = set(stopwords.words('english'))

    # Process content
    words = nltk.word_tokenize(content.lower())
    keywords = [word for word in words if word.isalnum() and word not in stop_words]

    # Display top keywords
    vectorizer = CountVectorizer(max_features=10)
    X = vectorizer.fit_transform([' '.join(keywords)])
    print("Top Keywords:", vectorizer.get_feature_names_out())

    # 3. Generating new content using AI
    if transformers_installed:
        try:
            # Using the publicly available GPT-2 model
            generator = pipeline("text-generation", model="gpt2")
            generated_content = generator("How to improve SEO using AI?", max_length=100, num_return_sequences=1)
            print("Generated Content:", generated_content[0]['generated_text'])
        except Exception as e:
            print("Error generating content with GPT-2:", e)
            generated_content = "Unable to generate content at this time."
    else:
        generated_content = "AI content generation skipped due to missing library."

    # 4. Final Report
    print("\n--- Final Report ---")
    print("Title:", title)
    print("Meta Description:", meta_desc)
    print("Generated Content (if available):", generated_content)
else:
    print("No content available to analyze.")
