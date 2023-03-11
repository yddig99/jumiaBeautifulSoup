from bs4 import BeautifulSoup

import requests

url ="https://www.jumia.co.ke/"

result = requests.get(url).text

soup = BeautifulSoup(result , "html.parser")

for link in soup.find_all('a'):

    print(link.get('href'))