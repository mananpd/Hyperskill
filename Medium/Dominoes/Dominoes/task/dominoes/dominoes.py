import random
from collections import Counter


class Dominos:
    """"""

    def __init__(self):
        self.full_set = []
        self.computer_set = []
        self.user_set = []
        self.stock_set = []
        self.snake = []
        self.status = None
        self.main()
        self.computer_score = []

    def generate_dominos(self):
        for i in range(7):
            for j in range(i, 7):
                domino = [i, j]
                self.full_set.append(domino)

    def split_dominos(self):
        random.shuffle(self.full_set)
        for _ in range(14):
            self.stock_set.append(self.full_set.pop())
        for _ in range(7):
            self.user_set.append(self.full_set.pop())
        self.computer_set = self.full_set

    def first_move(self):
        while True:
            for domino in self.computer_set:
                if domino[0] == domino[1]:
                    if not self.snake:
                        self.snake = domino
                    elif self.snake[0] < domino[0]:
                        self.snake = domino
            for domino in self.user_set:
                if domino[0] == domino[1]:
                    if not self.snake:
                        self.snake = domino
                    elif self.snake[0] < domino[0]:
                        self.snake = domino
            if self.snake in self.computer_set:
                self.computer_set.remove(self.snake)
                self.status = "player"
                self.snake = [self.snake]
                break
            elif self.snake in self.user_set:
                self.user_set.remove(self.snake)
                self.status = "computer"
                self.snake = [self.snake]
                break
            else:
                self.generate_dominos()
                self.split_dominos()

    def check_move(self, choice):
        if self.status == "player":
            status_set = self.user_set
        else:
            status_set = self.computer_set
        while True:
            if choice == 0 and len(self.stock_set) == 0:
                break
            elif choice == 0 and self.status == "player" and len(self.stock_set) > 0:
                self.user_set.append(self.stock_set.pop())
                break
            elif choice == 0 and self.status == "computer" and len(self.stock_set) > 0:
                self.computer_set.append(self.stock_set.pop())
                break
            elif choice < 0:
                if status_set[abs(choice) - 1][1] == self.snake[0][0]:
                    self.snake.insert(0, status_set.pop(abs(choice) - 1))
                    return True
                elif status_set[abs(choice) - 1][0] == self.snake[0][0]:
                    self.snake.insert(0, status_set.pop(abs(choice) - 1)[::-1])
                    return True
                else:
                    if self.status == "player":
                        print("Illegal move. Please try again.")
                        choice = int(input())
                    else:
                        return False
            elif choice > 0:
                if status_set[choice - 1][0] == self.snake[len(self.snake) - 1][1]:
                    self.snake.append(status_set.pop(abs(choice) - 1))
                    return True
                elif status_set[choice - 1][1] == self.snake[len(self.snake) - 1][1]:
                    self.snake.append(status_set.pop(abs(choice) - 1)[::-1])
                    return True
                else:
                    if self.status == "player":
                        print("Illegal move. Please try again.")
                        choice = int(input())
                    else:
                        return False

    def computer_move(self):
        list_set = []
        for domino in (self.computer_set + self.stock_set):
            list_set.append(domino[0])
            list_set.append(domino[1])
        total_scores = Counter(list_set)
        computer_score = []
        computer_score_check = []
        index_range = []
        for i in range(len(self.computer_set)):
            score = total_scores[self.computer_set[i][0]] + total_scores[self.computer_set[i][1]]
            computer_score.append(score)
            if self.computer_set[i][0] == self.snake[0][0]:
                computer_score_check.append(True)
                index_range.append(-i - 1)
            elif self.computer_set[i][1] == self.snake[0][0]:
                computer_score_check.append(True)
                index_range.append(-i - 1)
            elif self.computer_set[i][0] == self.snake[len(self.snake) - 1][1]:
                computer_score_check.append(True)
                index_range.append(i + 1)
            elif self.computer_set[i][1] == self.snake[len(self.snake) - 1][1]:
                computer_score_check.append(True)
                index_range.append(i + 1)
            else:
                computer_score_check.append(False)
                index_range.append(0)
        computer_score_check = [x for _, x in sorted(zip(computer_score, computer_score_check))]
        index_range = [x for _, x in sorted(zip(computer_score, index_range))]
        computer_score_check.reverse()
        index_range.reverse()
        computer_score.sort()
        computer_score.reverse()
        for i in range(len(computer_score)):
            if computer_score_check[i]:
                return index_range[i]
        return 0

    def next_move(self):
        if self.status == "computer" and len(self.computer_set) > 0:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            input()
            computer_choice = self.computer_move()
            self.check_move(computer_choice)
            self.status = "player"
            return True
        elif self.status == "player" and len(self.user_set) > 0:
            print("Status: It's your turn to make a move. Enter your command.")
            while True:
                try:
                    user_choice = int(input())
                    if (abs(user_choice)) > len(self.user_set):
                        print("Invalid input. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please try again.")
            self.check_move(user_choice)
            self.status = "computer"
            return True
        else:
            return False

    def interface(self):
        print("=" * 70)
        print(f"Stock size: {len(self.stock_set)}")
        print(f"Computer pieces: {len(self.computer_set)}")
        print()
        if len(self.snake) > 6:
            print(*self.snake[0:3], "...", *self.snake[(len(self.snake) - 3):], sep ="")
        else:
            print(*self.snake, sep="")
        print()
        print("Your pieces:")
        for i in range(len(self.user_set)):
            print(f"{i + 1}: {self.user_set[i]}")
        print()

    def is_game_finished(self):
        if len(self.user_set) == 0:
            print("Status: The game is over. You won!")
            return True
        elif len(self.computer_set) == 0:
            print("Status: The game is over. The computer won!")
            return True
        elif self.snake[0][0] == self.snake[len(self.snake) - 1][1]:
            count = 0
            for domino in self.snake:
                if domino[0] == self.snake[0][0]:
                    count += 1
                if domino[1] == self.snake[0][0]:
                    count += 1
            print(count)
            if count > 7:
                print("Status: The game is over. It's a draw!")
                return True
            else:
                return False
        else:
            return False

    def main(self):
        self.generate_dominos()
        self.split_dominos()
        self.first_move()
        self.interface()
        counter = 0
        while True:
            self.next_move()
            self.interface()
            if self.is_game_finished():
                break
            counter += 1
            if counter == 50:
                print("Status: The game is over. It's a draw!")
                break

dominos = Dominos()
