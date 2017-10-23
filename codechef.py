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
long_ch=t.findAll('td')
cnt=0
for ln in long_ch:
	if cnt==1:
		print("Long Challenge = ",ln.text)
	elif cnt ==5:
		print("Cook Off   \t   = ",ln.text)
	elif cnt == 9:
		print("Lunch Time     = ",ln.text)
	cnt=(cnt+1)
