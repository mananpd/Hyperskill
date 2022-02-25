import random


class RockPaperScissors:

    def __init__(self):
        self.name = None
        self.score = 0
        self.user = None
        self.computer = None
        self.winner = None
        self.game = None
        self.outcomes = {}
        self.main()

    def user_name(self):
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}")

    def user_game(self):
        self.game = input().split(sep=",")
        if self.game == [""]:
            self.game = 'rock,paper,scissors'.split(sep=",")
        extended_game = self.game * 3
        for sign in self.game:
            first_index = self.game.index(sign) + 1
            last_index = first_index + int((len(self.game) - 1) / 2)
            upper_signs = extended_game[first_index:last_index]
            sign_dict = {f"{sign}": upper_signs}
            self.outcomes.update(sign_dict)
        print("Okay, let's start")

    def user_score(self):
        score_file = open("rating.txt", "r")
        for line in score_file:
            name, previous_score = line.split()
            if name == self.name:
                self.score = int(previous_score)

    def play(self):
        while True:
            self.user = input()
            if self.user == "!exit":
                print("Bye!")
                exit()
            if self.user == "!rating":
                print(f"Your rating: {self.score}")
            elif self.user in list(self.outcomes.keys()):
                self.computer = random.choice(list(self.outcomes.keys()))
                break
            else:
                print("Invalid input")

    def who_wins(self):
        if self.computer in self.outcomes[self.user]:
            self.winner = "computer"
        elif self.computer == self.user:
            self.winner = "draw"
            self.score += 50
        else:
            self.winner = "user"
            self.score += 100

    def main(self):
        self.user_name()
        self.user_score()
        self.user_game()
        while True:
            self.play()
            self.who_wins()
            if self.winner == "computer":
                print(f"Sorry, but the computer chose {self.computer}")
            elif self.winner == 'draw':
                print(f"There is a draw ({self.computer})")
            else:
                print(f"Well done. The computer chose {self.computer} and failed")


RockPaperScissors()
