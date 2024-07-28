import requests
from bs4 import BeautifulSoup
import json
import datetime
import os

# Initial settings
url = 'https://www.bbc.com/news'
keywords = ['analysis', 'Gaza']  # Example for filtering news
output_format = 'json'  # or 'csv'
output_file = f'headlines_{datetime.datetime.now().strftime("%Y-%m-%d")}.{output_format}'

# Fetching and parsing the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Collecting news information
news_items = []
# Attempting to find a more reliable way to identify news items, 
# This might require adjustments
for article in soup.find_all('a', href=True):
    headline = article.text.strip() if article.text else 'No Title'
    link = article['href']
    summary = ''  # BBC News might not provide summaries in a consistent manner accessible from the homepage

    # Correcting relative links to absolute
    if link.startswith('/'):
        link = 'https://www.abc.net.au/news' + link

    # Filtering news based on keywords
    if any(keyword.lower() in headline.lower() for keyword in keywords):
        news_item = {
            'headline': headline,
            'summary': summary,  # Note: Summary might be empty
            'link': link,
        }
        news_items.append(news_item)

# Saving the collected information
if os.path.exists(output_file):
    with open(output_file, 'r', encoding='utf-8') as file:
        existing_data = json.load(file)
        news_items.extend(existing_data)
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(news_items, file, ensure_ascii=False, indent=4)

print(f'News items have been saved in the file {output_file}.')

# Reading the JSON file and displaying its content
with open(output_file, 'r', encoding='utf-8') as file:
    saved_news_items = json.load(file)

print("\nContent of the JSON file:")
for item in saved_news_items:
    print(f"Headline: {item['headline']}\nSummary: {item['summary']}\nLink: {item['link']}\n")
