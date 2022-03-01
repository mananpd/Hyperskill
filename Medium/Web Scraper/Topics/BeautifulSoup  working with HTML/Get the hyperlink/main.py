import requests
from bs4 import BeautifulSoup

index = int(input())
url = input()
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find_all('a')[index - 1].get('href'))
