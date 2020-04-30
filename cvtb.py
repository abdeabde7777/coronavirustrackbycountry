from requests import get
from bs4 import BeautifulSoup as bs

print("********<Corana stats>**********")
country=input("Country: ")
link=("https://www.worldometers.info/coronavirus/country/")
url=(link+country+"/")

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
handi=list()

try:
    d = get(url, headers=hdr)
    soup = bs(d.content, 'html.parser')
    payload = soup('span')
    for tag in payload:
        handi.append(tag)
except:
    print("error")

x=handi[4]
cases=x.contents[0]

x2=handi[5]
deaths=x2.contents[0]

print("********************************")
print("Coronavirus Cases: ", cases)
print("Deaths: ", deaths)
print("********************************")
