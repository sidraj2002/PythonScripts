import requests
from bs4 import BeautifulSoup
from pprint import pprint

def WebScraper(URL, data):
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    webdata = requests.get(URL, headers=headers)
    #print(webdata.text)
    return webdata
def SoupPriceChecker(webdata):
    mydata = []

    html = BeautifulSoup(webdata.text, 'html.parser')
    #test = html.body.main.article
    test = html.find_all('a', {"ProductLink_645485"})
    if test.find_all('a', {'data-price'} ) == "499.99":
        print(True)
    
    #print(html.body.main.article.prettify())
    #print(test)

    
mydata = WebScraper('https://www.microcenter.com/category/4294967288,4294820432,4294816489/macbook-air', 'Rekognition')
SoupPriceChecker(mydata)