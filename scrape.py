import requests
from bs4 import BeautifulSoup

# Requests allow us to download the html
# BeautifulSoup allow us to scrape, manage the request data

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_hm(links, votes):
    hn = []
