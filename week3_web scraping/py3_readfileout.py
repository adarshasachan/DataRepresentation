import requests
from bs4 import BeautifulSoup

with open("../week2/carviwer.html")as fp:
    soup=BeautifulSoup(fp,'html.parser')
#print(soup.tr)
rows=soup.findAll("tr")
for row in rows:
    #print("_____________")
    #print(row)
    dataset=[]
    cols=row.findAll("td")
    for col in cols:
        dataset.append(col.text)
    print(dataset)