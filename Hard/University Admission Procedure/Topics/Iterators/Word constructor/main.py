word1 = input()
word2 = input()

word1_word2 = ""
for l1, l2 in zip(word1, word2):
    word1_word2 = word1_word2 + l1 + l2

print(word1_word2)
