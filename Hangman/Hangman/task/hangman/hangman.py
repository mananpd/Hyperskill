import random


class Hangman:
    WORDS = ('python', 'java', 'kotlin', 'javascript')

    def __init__(self):
        self.answer = random.choice(self.WORDS)
        self.guess = [char for char in "-" * len(self.answer)]
        self.guessed_letters = []

    def __str__(self):
        return "H A N G M A N"

    def one_turn(self):
        if "".join(self.guess) == self.answer:
            print("You guessed the word!\n"
                  "You survived!")
            return 1
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            return 0
        elif letter.isupper() or not letter.isalpha():
            print("Please enter a lowercase English letter")
            return 0
        elif letter in self.guessed_letters:
            print("You've already guessed this letter")
            return 2
        elif letter in self.answer:
            self.guessed_letters.append(letter)
            for i in range(len(self.answer)):
                if self.answer[i] == letter:
                    self.guess[i] = letter
            return 3
        else:
            self.guessed_letters.append(letter)
            print("That letter doesn't appear in the word")
            return 4

    def play(self):
        counter = 8
        while counter > 0:
            print()
            print("".join(self.guess))
            turn = self.one_turn()
            if turn == 1:
                break
            elif turn == 4:
                counter -= 1
        if "".join(self.guess) != self.answer:
            print("You lost!")

    def main(self):
        while True:
            to_play = input('Type "play" to play the game, "exit" to quit:')
            if to_play == 'play':
                self.play()
                self.__init__()
            if to_play == 'exit':
                exit()
            else:
                continue


hangman = Hangman()
print(hangman)
hangman.main()
