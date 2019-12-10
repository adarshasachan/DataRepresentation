import requests
from bs4 import BeautifulSoup

with open("../week2/carviwer.html")as fp:
    soup=BeautifulSoup(fp,'html.parser')
print(soup.prettify())