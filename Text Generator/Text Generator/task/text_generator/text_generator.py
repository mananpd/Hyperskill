import nltk
import random
import re


class TextGenerator:
    def __init__(self):
        self.file = None
        self.text = None
        self.token = None
        self.trigrams = None
        self.markov_dic = {}
        self.head = None
        self.main()

    def get_input(self):
        self.file = input()
        f = open(self.file, "r", encoding="utf-8")
        self.text = f.read()
        f.close()

    def get_token(self):
        self.token = self.text.split()

    def get_trigrams(self):
        self.trigrams = list(nltk.trigrams(self.token))

    def create_markov_model(self):
        for head, middle, tail in self.trigrams:
            key = head + " " + middle
            self.markov_dic.setdefault(key, {}).setdefault(tail, 0)
            self.markov_dic[key][tail] += 1

    def create_random_text(self):
        while True:
            if self.head is None:
                token = random.choice(self.trigrams)
                self.head = token[0] + " " + token[1]
            elif re.match('^[A-Z][^?!.]*[^?.!]$', self.head) is None:
                token = random.choice(self.trigrams)
                self.head = token[0] + " " + token[1]
            else:
                break
        sentence = [self.head]
        counter = 0
        while True:
            if counter == 0:
                head = sentence[counter]
            elif counter == 1:
                head = self.head.split()[1] + " " + sentence[counter]
            else:
                head = sentence[counter - 1] + " " + sentence[counter]

            word = random.choices(list(self.markov_dic[head].keys()),
                                  list(self.markov_dic[head].values()))[0]
            sentence.append(word)
            if len(sentence) > 3 and re.match('^[^?!.]*[?.!]$', sentence[counter + 1]) is not None:
                break
            counter += 1
        self.head = None
        print(*sentence)

    def main(self):
        self.get_input()
        self.get_token()
        self.get_trigrams()
        self.create_markov_model()
        for _ in range(10):
            self.create_random_text()


TextGenerator()
