import requests
from bs4 import BeautifulSoup
import sys


class Translator:
    def __init__(self):
        self.args = sys.argv
        self.source_language = None
        self.output_language = []
        self.word = None
        self.url = 'https://context.reverso.net/translation/'
        self.soup = []
        self.word_translation = []
        self.examples = []
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.supported_languages = {1: "Arabic", 2: "German", 3: "English", 4: "Spanish", 5: "French",
                                    6: "Hebrew", 7: "Japanese", 8: "Dutch", 9: "Polish", 10: "Portuguese",
                                    11: "Romanian", 12: "Russian", 13: "Turkish"}
        self.main()

    def input_language(self):
        # print('Type the number of your language: ')
        source_language = self.args[1]
        lower_languages = []
        for language in self.supported_languages.values():
            lower_languages.append(language.lower())
        self.source_language = source_language
        # print('Type the number of a language you want to translate to or "0" to translate to all languages:')
        output_language = self.args[2]
        if output_language == 'all':
            for language in self.supported_languages.values():
                if language.lower() != self.source_language.lower():
                    self.output_language.append(language)
        elif source_language not in lower_languages:
            print(f"Sorry, the program doesn't support {source_language}")
            exit()
        elif output_language not in lower_languages:
            print(f"Sorry, the program doesn't support {output_language}")
            exit()
        else:
            self.output_language.append(output_language)

    def input_word(self):
        # print('Type the word you want to translate:')
        self.word = self.args[3]

    def print_message(self):
        print(f"Hello, you're welcome to the translator. Translator supports:")
        for num, language in self.supported_languages.items():
            print(f"{num}.", language)

    def connect_to_translator(self):
        for language in self.output_language:
            try:
                url = self.url + self.source_language.lower() + '-' + language.lower()
                url = url + "/" + self.word
                response = requests.get(url, headers=self.headers)
                print(response.status_code)
                if response.status_code == 200:
                    self.soup.append(BeautifulSoup(response.content, 'html.parser'))
                else:
                    print(f'Sorry, unable to find {self.word}')
                    exit()
            except requests.exceptions.ConnectionError:
                print("Something wrong with your internet connection")
                exit()

    def translation(self):
        for soup in self.soup:
            words = soup.find('div', {'id': 'translations-content'}).text.replace("\n", "").replace("\r", "").split("          ")
            words = words[1:len(words)]
            self.word_translation.append(words)
            source_example = soup.find_all('div', {'class': 'src ltr'})
            translated_example = soup.find_all('div', {'class': 'trg'})
            examples = []
            for i in range(len(source_example)):
                examples.append(source_example[i].text.strip())
                examples.append(translated_example[i].text.strip())
            self.examples.append(examples)

    def print_translations(self):
        for i in range(len(self.output_language)):
            print(f'{self.output_language[i]} Translations:')
            if len(self.output_language) == 1:
                for word in self.word_translation[i]:
                    print(word)
            else:
                print(self.word_translation[i][0])
            print()
            print(f'{self.output_language[i]} Examples:')
            if len(self.output_language) == 1:
                for j in range(0, len(self.examples[i]), 2):
                    print(self.examples[i][j])
                    print(self.examples[i][j + 1])
            else:
                print(self.examples[i][0])
                print(self.examples[i][1])
            print()

    def save_translation(self):
        with open(f"{self.word}.txt", "w") as file:
            for i in range(len(self.output_language)):
                file.write(f'{self.output_language[i]} Translations:\n')
                if len(self.output_language) == 1:
                    for word in self.word_translation[i]:
                        file.write(word + '\n')
                else:
                    file.write(self.word_translation[i][0] + '\n')
                file.write("\n")
                file.write(f'{self.output_language[i]} Examples:\n')
                if len(self.output_language) == 1:
                    for j in range(0, len(self.examples[i]), 2):
                        file.write(self.examples[i][j] + '\n')
                        file.write(self.examples[i][j + 1] + '\n')
                else:
                    file.write(self.examples[i][0] + '\n')
                    file.write(self.examples[i][1] + '\n')
                file.write("\n")

    def main(self):
        # self.print_message()
        self.input_language()
        self.input_word()
        self.connect_to_translator()
        self.translation()
        self.print_translations()
        self.save_translation()


translator = Translator()
