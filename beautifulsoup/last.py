# to go to url = https://en.wikipedia.org/wiki/Main_Page
# get list of bold text0

import requests
from bs4 import BeautifulSoup
import html5lib


url="https://en.wikipedia.org/wiki/Main_Page"
req=requests.get(url)
#print(req.content())

sp=BeautifulSoup(req.content,'html5lib')
#print(sp.prettify())

t=[]
t=sp.findAll('span',{'class':'mw-headline'})
#print(t[0])
for i in range(len(t)):
    if t[i].get_text()=="Did you know ...":
        print(t[i])


y=sp.findAll('div',{'id':'mp-otd'})
y1 = y[0]
print(y1.get_text())
