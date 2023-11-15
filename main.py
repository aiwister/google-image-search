import requests
from bs4 import BeautifulSoup as bs
q="abcde"
url=f"https://www.google.com/search?q={q}&tbm=isch"
soup=bs(requests.get(url).text,"html.parser")
img=soup.select("a > div.kCmkOe > img")
for i in img[:5]:
    print(i["src"])
