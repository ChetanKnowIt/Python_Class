
'''
Installation of library
pip install bs4
pip install requests
pip install html5lib
'''

import requests
from bs4 import BeautifulSoup
import html5lib

# ========= step1
url="https://www.passiton.com/inspirational-quotes"
req=requests.get(url)
#print(req.content)

# ========= step2 
sp=BeautifulSoup(req.content,'html5lib')
#print(sp.prettify())


tbl=sp.find('div',{'id':'all_quotes'})
lineno=0
for row in tbl.findAll('div'):
    lineno=lineno+1
    cnt=row.find('img')
    lst=cnt['alt'].split('#')
    print(lineno,". ",lst[0])







