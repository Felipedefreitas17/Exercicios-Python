import requests
from bs4 import BeautifulSoup

html = requests.get("https://dolarhoje.com/").content

#print(html)

soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify())

dolar = soup.find(id="nacional")

print(dolar['value'])