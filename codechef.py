import requests
from bs4 import BeautifulSoup

handle='bansal1232'
url='https://www.codechef.com/users/'+handle
r=requests.get(url)

soup=BeautifulSoup(r.content,'lxml')
t=soup.find('aside', class_='sidebar small-4 columns pr0')
overall=t.find('div',attrs={'class':'rating-number'})
print("Overall Rating = ",overall.text)
print("\nIndividual Ratings")
Ratings=t.findAll('td')
print("Long Challenge = ",Ratings[1].text)
print("Cook Off   \t   = ",Ratings[5].text)
print("Lunch Time     = ",Ratings[9].text)
