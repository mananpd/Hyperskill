import os

import requests
from bs4 import BeautifulSoup
import re


class Scraper:
    def __init__(self):
        self.num_of_pages = None
        self.type_of_article = None
        self.response = []
        self.soup = None
        self.title = []
        self.links = []
        self.type = []
        self.body = []
        self.url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page="

    def get_response(self, page):
        try:
            self.response = requests.get(self.url + str(page), headers={'Accept-Language': 'en-US,en;q=0.5'})
            if self.response.status_code != 200:
                print("Invalid page!")
        except requests.exceptions.ConnectionError:
            print("Connection error")

    def parse(self, what_to_parse):
        try:
            self.soup = BeautifulSoup(self.response.content, 'html.parser')
            article_type = self.soup.find_all('span', {'class': 'c-meta__type'})
            article_title = self.soup.find_all('h3', {"class": "c-card__title", "itemprop": "name headline"})
            article_links = self.soup.find_all('a', {"class": "c-card__link u-link-inherit", "itemprop": "url"})
            for index in range(len(article_type)):
                if article_type[index].text == what_to_parse:
                    self.type.append(article_type[index].text)
                    title_formatted = article_title[index].text
                    title_formatted = re.sub(r'[^\w\s]', '', title_formatted.replace("\n", ""))
                    title_formatted = title_formatted.replace(" ", "_")
                    self.title.append(title_formatted)
                    self.links.append('https://www.nature.com' + article_links[index].get('href'))
            for link in self.links:
                article_response = requests.get(link, headers={'Accept-Language': 'en-US,en;q=0.5'})
                article_soup = BeautifulSoup(article_response.content, 'html.parser')
                self.body.append(article_soup.find_all("div", {'class': "c-article-body u-clearfix"})[0].text)
        except AttributeError:
            print("Invalid page!")

    def save_file(self, page):
        os.makedirs(f'Page_{page}')
        for i in range(len(self.title)):
            with open(f"Page_{page}/{self.title[i]}.txt", "w") as file:
                file.write(self.body[i])

    def main(self):
        self.num_of_pages = int(input())
        self.type_of_article = input()
        for i in range(self.num_of_pages):
            self.get_response(i + 1)
            self.parse(self.type_of_article)
            self.save_file(i + 1)
            self.__init__()


Scraper().main()
