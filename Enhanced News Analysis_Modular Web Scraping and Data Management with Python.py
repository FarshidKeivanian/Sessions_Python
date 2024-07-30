import requests
from bs4 import BeautifulSoup
import json
import datetime
import os

# Initial settings
url = 'https://www.abc.net.au/news'
keywords = ['analysis', 'Gaza']  # Example for filtering news
output_format = 'json'  # or 'csv'
output_file = f'headlines_{datetime.datetime.now().strftime("%Y-%m-%d")}.{output_format}'

# Function to fetch and parse the website
def fetch_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

# Function to collect news information
def collect_news(soup, keywords):
    news_items = []
    for article in soup.find_all('a', href=True):
        headline = article.text.strip() if article.text else 'No Title'
        link = article['href']
        summary = ''  # ABC News might not provide summaries in a consistent manner

        # Correcting relative links to absolute
        if link.startswith('/'):
            link = 'https://www.abc.net.au' + link

        # Filtering news based on keywords
        if any(keyword.lower() in headline.lower() for keyword in keywords):
            news_item = {
                'headline': headline,
                'summary': summary,
                'link': link,
            }
            news_items.append(news_item)
    return news_items

# Function to save news items to a JSON file
def save_news(news_items, output_file):
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        try:
            with open(output_file, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
                news_items.extend(existing_data)
        except json.JSONDecodeError:
            print("Error decoding JSON from the file. Starting with an empty list.")
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(news_items, file, ensure_ascii=False, indent=4)

# Function to display saved news items
def display_news(output_file):
    try:
        with open(output_file, 'r', encoding='utf-8') as file:
            saved_news_items = json.load(file)
        print("\nContent of the JSON file:")
        for item in saved_news_items:
            print(f"Headline: {item['headline']}\nSummary: {item['summary']}\nLink: {item['link']}\n")
    except json.JSONDecodeError:
        print("Error reading the JSON file.")

# Main function to orchestrate the workflow
def main():
    soup = fetch_news(url)
    if soup:
        news_items = collect_news(soup, keywords)
        save_news(news_items, output_file)
        print(f'News items have been saved in the file {output_file}.')
        display_news(output_file)

# Run the main function
if __name__ == "__main__":
    main()
