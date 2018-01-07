import requests,re
from bs4 import BeautifulSoup

def codeforces_rating(handle):
	
	url='http://codeforces.com/profile/'+handle
	try:
		r=requests.get(url)
		soup=BeautifulSoup(r.content,'lxml')
		t=soup.find('div',class_='info').findAll('span', class_=re.compile('^user-'))
		return t[1].text
	except:
		return "User name is invalid"

if __name__=='__main__':
	handle='bansal1232'
	print("Overall Rating = ", codeforces_rating(handle))