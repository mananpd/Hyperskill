# put your python code here
line = input().lower().split()
unique_words = dict.fromkeys(line)
for words in unique_words.keys():
    unique_words[words] = line.count(words)
for word, value in unique_words.items():
    print(word, value)
