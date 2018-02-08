import requests
from bs4 import BeautifulSoup

def get_rating(handle):
	try:
		url='https://www.codechef.com/users/'+handle
		r=requests.get(url)

		soup=BeautifulSoup(r.content,'lxml')
		t=soup.find('aside', class_='sidebar small-4 columns pr0')
		overall=t.find('div',attrs={'class':'rating-number'})
		Ratings=t.findAll('td')
		string='''Overall Rating = {}

Individual Ratings
Long Challenge =  {}
Cook Off   \t   = {}
Lunch Time     = {}'''.format(overall.text,Ratings[1].text,Ratings[5].text,Ratings[9].text)
	except:
		string='Something might went wrong! Please check Username or Internet Connection'
	return string
if __name__=='__main__':
	handle='bansal1232'
	print(get_rating(handle))
