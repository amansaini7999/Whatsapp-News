'''import time

time.localtime(time.time())

mn = time.localtime(time.time()).tm_mon

if(mn==1):
    mon = "jan"

elif(mn==2):
    mon = "feb"

elif(mn==3):
    mon = "mar"

elif(mn==4):
    mon = "apr"

elif(mn==5):
    mon = "may"

elif(mn==6):
    mon = "jun"

elif(mn==7):
    mon = "jul"

elif(mn==8):
    mon = "aug"

elif(mn==9):
    mon = "sep"

elif(mn==10):
    mon = "oct"

elif(mn==11):
    mon = "nov"

elif(mn==12):
    mon = "dec"


year = time.localtime(time.time()).tm_year
year

date = time.localtime(time.time()).tm_mday
date

from bs4 import BeautifulSoup as BS

import requests
page = requests.get("https://epaper.dailyexcelsior.com/")

pageCount=15
if(page.status_code==200):
    soup = BS(page.content, 'html.parser')
    s = soup.find('div', id="scroller")
    pageCount=len(s.select('ul', class_='epapertest')[0].select('li'))

pageCount

for i in range(1, pageCount):
    url = https://epaper.dailyexcelsior.com/epaperpdf/{}/{}/{}{}{}/page{}.pdf.format(year, mon, str(year)[:2], mon, str(date).zfill(2), i)
    print(url)

from bs4 import BeautifulSoup as BS

import requests
page = requests.get("https://epaper.dailyexcelsior.com/")

pageCount=15
if(page.status_code==200):
    soup = BS(page.content, 'html.parser')
    s = soup.find('div', id="scroller")
    pageCount=len(s.select('ul', class_='epapertest')[0].select('li'))

pageCount


output = bytearray()

for i in range(1, pageCount):
    url = https://epaper.dailyexcelsior.com/epaperpdf/{}/{}/{}{}{}/page{}.pdf.format(year, mon, str(year)[:2], mon, str(date).zfill(2), i)
    #print(url)
    r = requests.get(url)
    output.extend(r.content)

f = open("sample1.pdf","wb")
f.write(output)
f.close()'''


def scrape():
    return 0