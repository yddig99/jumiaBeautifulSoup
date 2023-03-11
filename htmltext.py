import  requests

url = "https://www.jumia.co.ke/"

result = requests.get(url).text

print(result)


