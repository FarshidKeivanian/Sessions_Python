import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# Check and download nltk resources
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
    stop_words = set(stopwords.words('english'))

# 1. Collecting data from the website
def fetch_website_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

# 2. Parsing website content
def parse_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title
    title = soup.title.string.strip() if soup.title else "No title found"

    # Extract meta description
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    meta_desc = meta_tag['content'].strip() if meta_tag and 'content' in meta_tag.attrs else "No meta description found"

    # Remove unwanted tags and get text content
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    content = soup.get_text(separator=" ", strip=True)
    return title, meta_desc, content

# 3. Analyzing content
def analyze_content(content):
    try:
        words = nltk.word_tokenize(content.lower())
        keywords = [word for word in words if word.isalnum() and word not in stop_words]

        # Get top keywords using CountVectorizer
        vectorizer = CountVectorizer(max_features=10)
        X = vectorizer.fit_transform([' '.join(keywords)])
        top_keywords = vectorizer.get_feature_names_out()
        return top_keywords
    except Exception as e:
        print(f"Error analyzing content: {e}")
        return []

# Main program
if __name__ == "__main__":
    url = "https://newcastle.edu.au/"
    html_content = fetch_website_data(url)

    if html_content:
        title, meta_desc, content = parse_content(html_content)

        if content:
            print("\nAnalyzing Content...")
            top_keywords = analyze_content(content)
            print("\n--- Final Report ---")
            print("Title:", title)
            print("Meta Description:", meta_desc)
            print("Top Keywords:", ", ".join(top_keywords))
        else:
            print("No content available to analyze.")
    else:
        print("Failed to fetch or parse website content.")
