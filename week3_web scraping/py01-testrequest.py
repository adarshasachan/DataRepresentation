import requests
from bs4 import BeautifulSoup
page=requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
print(page)
print("========================")
print(page.content)
soup1=BeautifulSoup(page.content,"html.parser")
print(soup1.prettify())