import requests

#url='https://www.gmit.ie'
#responce=requests.get(url)
#print(responce.status_code)
##print(responce.headers)

url='http://127.0.0.1:5000/cars'
data={'reg':'123','make':'blah','model':'tine','price':1234}
response=requests.post(url,json=data)
print(response.status_code)
print(response.json())