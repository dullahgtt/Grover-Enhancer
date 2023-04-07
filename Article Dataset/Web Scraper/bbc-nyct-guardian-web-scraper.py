import requests
from bs4 import BeautifulSoup
import csv

# List of news websites to scrape
websites = ['https://www.nytimes.com/', 'https://www.bbc.com/', 'https://www.theguardian.com/us']

# CSV file to store the collected data
filename = 'news_articles.csv'

# Open the file for writing
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row to the file
    writer.writerow(['title', 'author', 'date_published', 'source', 'content'])

    for site in websites:
        # Send a request to the website
        response = requests.get(site)

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the articles on the page
        articles = soup.find_all('article')

        # Loop through each article and extract the relevant data
        for article in articles:
            # Extract the title of the article
            title = article.find('h2').text.strip()

            # Extract the author of the article, if available
            author = article.find('span', class_='css-1n7hynb').text.strip() if article.find('span', class_='css-1n7hynb') else ''

            # Extract the date the article was published, if available
            date_published = article.find('time')['datetime'] if article.find('time') else ''

            # Extract the source of the article
            source = site

            # Extract the content of the article
            content = article.find('p').text.strip() if article.find('p') else ''

            # Write the extracted data to the CSV file
            writer.writerow([title, author, date_published, source, content])
