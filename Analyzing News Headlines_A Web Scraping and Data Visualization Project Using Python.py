import requests
from bs4 import BeautifulSoup
import json
import datetime
import os
from urllib.parse import urljoin

# Initial settings
url = 'https://www.abc.net.au/news'
keywords = ['Australians']
output_file = f'headlines_{datetime.datetime.now().strftime("%Y-%m-%d")}.json'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Fetch page safely
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching website: {e}")
    raise SystemExit

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

news_items = []
seen_links = set()

# Collect links
for article in soup.find_all('a', href=True):
    headline = article.get_text(strip=True)
    link = article['href']

    if not headline:
        continue

    # Build absolute URL safely
    link = urljoin(url, link)

    # Skip duplicates
    if link in seen_links:
        continue

    # Filter by keyword in headline
    if any(keyword.lower() in headline.lower() for keyword in keywords):
        news_items.append({
            'headline': headline,
            'summary': '',
            'link': link
        })
        seen_links.add(link)

# Load old data if file exists
existing_data = []
if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    with open(output_file, 'r', encoding='utf-8') as file:
        try:
            existing_data = json.load(file)
        except json.JSONDecodeError:
            print("Warning: JSON file was invalid. Starting fresh.")

# Merge without duplicates
existing_links = {item['link'] for item in existing_data if 'link' in item}
for item in news_items:
    if item['link'] not in existing_links:
        existing_data.append(item)

# Save JSON
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(existing_data, file, ensure_ascii=False, indent=4)

print(f"News items have been saved in the file {output_file}.")

# Display saved content
with open(output_file, 'r', encoding='utf-8') as file:
    saved_news_items = json.load(file)

print("\nContent of the JSON file:")
for item in saved_news_items:
    print(f"Headline: {item['headline']}\nSummary: {item['summary']}\nLink: {item['link']}\n")
