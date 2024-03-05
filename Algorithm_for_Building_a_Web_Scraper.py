#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup

# The URL of the website we want to scrape data from
url = 'https://www.abc.net.au/news'

# Sending an HTTP GET request to the website
response = requests.get(url)

# Parsing the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all the news headlines on the page (assuming each headline is contained in an <h2> tag)
headlines = soup.find_all('h2')

# Opening a file to write
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for headline in headlines:
        # Writing each headline into the file
        file.write(headline.text.strip() + '\n')

print('Headlines have been saved in the file headlines.txt.')


# In[ ]:




