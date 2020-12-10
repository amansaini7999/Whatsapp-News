def extract_month(mn):
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

    return mon

def scrape():
    import time
    from PyPDF2 import PdfFileMerger
    import os

    current_time = time.localtime(time.time())

    mon = extract_month(current_time.tm_mon)
    year = current_time.tm_year
    date = current_time.tm_mday

    from bs4 import BeautifulSoup as BS
    import requests
    page = requests.get("https://epaper.dailyexcelsior.com/")

    pageCount=15
    if(page.status_code==200):
        soup = BS(page.content, 'html.parser')
        s = soup.find('div', id="scroller")
        pageCount=len(s.select('ul', class_='epapertest')[0].select('li'))

    for i in range(1, pageCount):
        url = '''https://epaper.dailyexcelsior.com/epaperpdf/{}/{}/{}{}{}/page{}.pdf'''.format(year, mon, str(year)[:2], mon, str(date).zfill(2), i)
        r = requests.get(url)
        f = open("temp/{}.pdf".format(i), "wb")
        f.write(r.content)
        f.close()
        time.sleep(1)

    pdfs = set()
    for element in os.listdir("temp/"):
        pdfs.add(int(element.split(".")[0]))

    pdfs = [str(i)+".pdf" for i in list(pdfs)]

    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append("temp/" + pdf)

    merger.write("temp/dailyexcelsior.pdf")
    merger.close()

    return 1

scrape()