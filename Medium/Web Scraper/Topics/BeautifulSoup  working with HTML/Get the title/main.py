import requests

from bs4 import BeautifulSoup

url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
h2 = soup.find('h1')
print(h2.text)
