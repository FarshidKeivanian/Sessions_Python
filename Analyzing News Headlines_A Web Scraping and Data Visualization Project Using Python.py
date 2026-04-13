import requests
from bs4 import BeautifulSoup
import json
import datetime
from urllib.parse import urljoin

# ---------------------------
# Settings
# ---------------------------
url = 'https://www.abc.net.au/news'
keywords = ['Australia', 'Australian', 'Australians']  # adjust if needed
output_file = f'headlines_{datetime.datetime.now().strftime("%Y-%m-%d")}.json'

headers = {'User-Agent': 'Mozilla/5.0'}

# ---------------------------
# Fetch Website
# ---------------------------
response = requests.get(url, headers=headers)
response.raise_for_status()

# ---------------------------
# Parse HTML
# ---------------------------
soup = BeautifulSoup(response.text, 'html.parser')

news_items = []
seen_links = set()

# ---------------------------
# Extract Headlines
# ---------------------------
for article in soup.find_all('a', href=True):
    headline = article.get_text(strip=True)
    link = urljoin(url, article['href'])

    if not headline or link in seen_links:
        continue

    if any(k.lower() in headline.lower() for k in keywords):
        news_items.append({
            'headline': headline,
            'link': link
        })
        seen_links.add(link)

# ---------------------------
# Save JSON
# ---------------------------
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(news_items, f, indent=4, ensure_ascii=False)

# ---------------------------
# Output
# ---------------------------
print(f"\nSaved {len(news_items)} news items to {output_file}\n")

for item in news_items:
    print(f"{item['headline']}\n{item['link']}\n")
