from bs4 import BeautifulSoup
import requests

Title = ""
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
            #print(href)
            #print(Title)
            file.write(href +" " + Title + '\n')
            get_item_info(href,Title)
            page_num = 122



def get_item_info(item_url,title):
    response = requests.get(item_url)
    plain_responce = response.text
    soup = BeautifulSoup(plain_responce)
    for item_desc in soup.findAll('time', {'class': 'timeago'}):
        #print(item_desc.string)
        file2.write(title + item_desc.string + '\n')


file = open('data.txt', 'w')
file2 = open('time.txt', 'w')

tread_spider(120)