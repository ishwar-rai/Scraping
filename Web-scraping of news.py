from bs4 import BeautifulSoup
import requests as rq


#url to scraped
url='https://timesofindia.indiatimes.com/'
res=rq.get(url)
soup=BeautifulSoup(res.text, "html.parser")

tag="tabcontent mostshared"
news=soup.find(class_=tag)


print(news.text)

for link in news.find_all('a'):
    print("https://timesofindia.indiatimes.com"+link.get('href'))

