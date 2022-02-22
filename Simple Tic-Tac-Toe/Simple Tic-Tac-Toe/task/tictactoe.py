class TicTacToe:
    def __init__(self):
        self.grid = [["_", "_", "_"],
                     ["_", "_", "_"],
                     ["_", "_", "_"]]
        self.grid_90 = [["_", "_", "_"],
                        ["_", "_", "_"],
                        ["_", "_", "_"]]
        self.outcome = None
        self.num_of_X = 0
        self.num_of_O = 0

        self.main()

    def __str__(self):
        return f"---------\n"\
               f"| {self.grid[0][0]} {self.grid[0][1]} {self.grid[0][2]} |\n" \
               f"| {self.grid[1][0]} {self.grid[1][1]} {self.grid[1][2]} |\n" \
               f"| {self.grid[2][0]} {self.grid[2][1]} {self.grid[2][2]} |\n" \
               f"---------\n"

    def play(self):
        while True:
            self.move()
            print(self.__str__())
            self.is_outcome()
            if self.outcome == "Game not finished":
                continue
            else:
                break

    def move(self):
        while True:
            player_move = input("Enter the coordinates:").split()
            try:
                j = int(player_move[0]) - 1
                i = int(player_move[1]) - 1
                if 0 <= i <= 2 and 0 <= j <= 2:
                    print(i)
                    print(j)
                    if self.grid[j][i] == "_":
                        self.grid[j][i] = "X"
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            except ValueError:
                print("You should enter numbers!")

    def rotate_grid(self):
        for i in range(3):
            for j in range(3):
                self.grid_90[j][i] = self.grid[i][j]

    def is_outcome(self):
        self.rotate_grid()
        if (any(x == ["X", "X", "X"] for x in self.grid) or any(x == ["X", "X", "X"] for x in self.grid_90)) and \
                (any(x == ["O", "O", "O"] for x in self.grid) or any(x == ["O", "O", "O"] for x in self.grid_90)):
            self.outcome = "Impossible"
        elif any(x == ["X", "X", "X"] for x in self.grid):
            self.outcome = "X wins"
        elif any(x == ["X", "X", "X"] for x in self.grid_90):
            self.outcome = "X wins"
        elif [self.grid[0][0], self.grid[1][1], self.grid[2][2]] == ["X", "X", "X"]:
            self.outcome = "X wins"
        elif [self.grid[2][0], self.grid[1][1], self.grid[0][2]] == ["X", "X", "X"]:
            self.outcome = "X wins"
        elif any(x == ["O", "O", "O"] for x in self.grid):
            self.outcome = "O wins"
        elif any(x == ["O", "O", "O"] for x in self.grid_90):
            self.outcome = "O wins"
        elif [self.grid[0][0], self.grid[1][1], self.grid[2][2]] == ["O", "O", "O"]:
            self.outcome = "0 wins"
        elif [self.grid[2][0], self.grid[1][1], self.grid[0][2]] == ["O", "O", "O"]:
            self.outcome = "0 wins"
        elif self.num_of_X == 5 or self.num_of_O == 5:
            self.outcome = "Draw"
        elif abs(self.num_of_X - self.num_of_O) <= 1:
            self.outcome = "Game not finished"
        else:
            self.outcome = "Impossible"

    def main(self):
        print(self.__str__())
        self.play()
        print(self.outcome)


tictactoe = TicTacToe()
