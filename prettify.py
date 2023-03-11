from bs4 import BeautifulSoup

import requests

url ="https://www.jumia.co.ke/"

result = requests.get(url).text

soup = BeautifulSoup(result , "html.parser")

print (soup.prettify())
