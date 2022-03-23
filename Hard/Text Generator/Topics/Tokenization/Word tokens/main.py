from nltk.tokenize import WordPunctTokenizer

sentence = input()
wpt = WordPunctTokenizer()
print(wpt.tokenize(sentence))
