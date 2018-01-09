import requests,re,os
from bs4 import BeautifulSoup
from tkinter import *
from codechef import get_rating
def code(handle):
  text.insert(INSERT,handle)
  text.insert(INSERT,handle,path)

def codechef_solutions(text,handle):
  if not os.path.exists(handle):
   os.makedirs(handle)
  codechef='https://www.codechef.com'
  url=codechef+'/users/'+handle
 #try:
  r=requests.get(url)
  #r=open('file','r')
  soup=BeautifulSoup(r.content,'lxml')
  #soup=BeautifulSoup(r,'lxml')

  t=soup.find('section',class_='rating-data-section problems-solved')
  link=t.findAll('a')
  cnt = 0 
  for x in link:

    prob = x.text
    pat=re.match('/+[\w]+/',x['href'])
    contest = pat.group(0)
    if(contest == '/status/'):
      contest='/Practice/'

    # Make directory of contest folder
    if not os.path.exists(handle+'/'+contest):
      os.makedirs(handle+contest)

    nxt_url=codechef+x['href']
    

    rqt=requests.get(nxt_url)
    soup=BeautifulSoup(rqt.content,'lxml')
    t=soup.find(href=re.compile("/viewsolution"))
    recall = 0
    while  t == None and recall < 3:
      text.insert(INSERT,"Trying Again",prob)
      rqt=requests.get(nxt_url)
      soup=BeautifulSoup(rqt.content,'lxml')
      t=soup.find(href=re.compile("^/viewsolution"))
      recall += 1
      pass
    
    if t == None:
      text.insert(INSERT,'Something Went wrong, may be solution of'+prob+'is not visible or might be there is some network problem\n')
      continue

    #Forward request to the solution
    headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    rqt_final=requests.get(codechef+t['href'],headers=headers,stream=True)
    soup=BeautifulSoup(rqt_final.content,'lxml')
    
    # Find language
    lang=soup.find('pre')

    # If language is not found, download in .text file
    if lang ==None:
      w = open(handle+contest+ prob + '.text')
      code = soup.find('div',id='solutiondiv')
      w.write(code.text)
      text.insert(INSERT,'Language not found,Successfully downloaded in .text file')
      continue

    w = open(handle+contest+prob+'.' + lang['class'][0], 'w')
    
    code=lang.findAll('li')
    for line in code:
      w.write(line.text+'\n')
    
    text.insert(INSERT,"Successfully Downloaded the"+prob+'\n')  
    cnt += 1
  return cnt
 #except:
  #return "Invalid username! Please try again"

if __name__=='__main__':
  #modi_0505

  #text.insert(INSERT,get_rating('bansal1232'))
  print('Total problems are: ',codechef_solutions('modi_0505'))