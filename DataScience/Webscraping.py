from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text,"html.parser")
for link in soup.find_all("a"):
    print(link.get("href"))
tags=soup("img")
for tag in tags:
    print(tag.get("src",None))
table = soup.find("table",{"class":"wikitable"})
df = pd.read_html(StringIO(str(table)))[0]
print(df[['Country (exonym)', 'Capital (exonym)', 'Official or native language(s) (alphabet/script)']].head(10))