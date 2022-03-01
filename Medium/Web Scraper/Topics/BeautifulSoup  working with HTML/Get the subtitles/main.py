import requests
from bs4 import BeautifulSoup

index = int(input())
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
h2 = soup.find_all('h2')[index]
print(h2.string)
