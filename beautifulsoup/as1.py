import requests
from bs4 import BeautifulSoup
import html5lib


url= "https://www.w3schools.com"
req=requests.get(url)
#print(req.content())


sp=BeautifulSoup(req.content,'html5lib')
#print(sp.prettify())

t = []
a1 = []
t = sp.findAll('h3',{'class':'w3-margin-top'})
for i in range(0, len(t)):
    a1.append(t[i].get_text())

#for 1st
print("1st: ",a1)

e = sp.findAll('div',{'class':'w3-col'})
a = e[0]
#print(a)

a2 = []
for i in a.findAll('a'):
    if i.get_text()=="Learn AI":
        break
    else:
        a2.append(i.get_text())


#for 2nd
print("2nd: ",a2)

