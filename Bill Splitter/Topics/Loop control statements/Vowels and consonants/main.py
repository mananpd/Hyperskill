from string import ascii_letters

vowel = ["a", "e", "i", "o", "u"]

phrase = input()
for letter in phrase:
    if letter in vowel:
        print("vowel")
    elif letter in ascii_letters:
        print("consonant")
    else:
        break
