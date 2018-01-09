import requests
from bs4 import BeautifulSoup

handle='bansal1232'
url='https://www.hackerearth.com/@'+handle
r=requests.get(url)
#print(r.text)

soup=BeautifulSoup(r.text,'lxml')
soup.findAll
number=soup.findAll('span',class_='track-following-num')
print('Hackerearth Rating =',number[1].text)
