import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
init()


class Browser:
    def __init__(self):
        self.args = sys.argv
        self.file_dir = self.args[1]
        self.url = None
        self.response = None
        self.soup = None
        self.main()

    def make_dir(self):
        if not os.access(self.file_dir, os.F_OK):
            os.mkdir(self.file_dir)

    def url_input(self):
        self.url = input()
        if not self.url.startswith("https://"):
            url = "https://" + self.url
            self.get_request(url)

    def get_request(self, url):
        try:
            self.response = requests.get(url)
            self.soup = BeautifulSoup(self.response.content, 'html.parser')
        except requests.exceptions.ConnectionError:
            print("Incorrect URL")
            exit()

    def print_response(self):
        print()
        a = self.soup.find_all("a")
        for i in range(len(a)):
            if a[i].string is not None:
                print(Fore.BLUE + a[i].string)

    def main(self):
        self.make_dir()
        self.url_input()
        self.print_response()


Browser()
