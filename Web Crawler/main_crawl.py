from bs4 import BeautifulSoup
import requests


def tread_spider(page_num):
    s=120
    while s <= page_num:
        url = 'https://sfbay.craigslist.org/search/bia?s=' + str(s)
        response = requests.get(url)
        plain_responce = response.text
        soup = BeautifulSoup(plain_responce)
        for link in soup.findAll('a', {'class': 'result-title hdrlnk'}):
            href = "https://sfbay.craigslist.org" + link.get('href')
            Title = link.string
            print(href)
            print(Title)
            file.write(href +" " + Title + '\n')

        page_num = 122


file = open('data.txt', 'w')
tread_spider(120)