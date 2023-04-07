import requests
from bs4 import BeautifulSoup

# Set the URL of the news website
url = "https://www.bbc.com/news"

# Send a request to the website and get the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links to news articles on the website
links = soup.find_all('a', class_='gs-c-promo-heading')

# Loop through each link and print the article title and URL
for link in links:
    article_title = link.text.strip()
    article_url = link['href']
    print(article_title)
    print(article_url)
