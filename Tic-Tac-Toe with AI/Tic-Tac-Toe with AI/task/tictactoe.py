import random


class TicTacToe:
    def __init__(self):
        self.board = [["_"] * 3] * 3
        self.turn = None
        self.main()

    def initial_state(self):
        state = input()
        self.board[0] = [turn for turn in state[0:3]]
        self.board[1] = [turn for turn in state[3:6]]
        self.board[2] = [turn for turn in state[6:9]]

    def print_board(self):
        print('---------')
        for row in self.board:
            print("|", end=" ", )
            for ij in row:
                if ij == "_":
                    print(" ", end=" ")
                else:
                    print(ij, end=" ")
            print("|")
        print('---------')

    def whose_turn(self):
        counter_X = 0
        counter_O = 0
        for row in self.board:
            for ij in row:
                if ij == "X":
                    counter_X += 1
                elif ij == "O":
                    counter_O += 1
        if counter_X == counter_O:
            self.turn = "X"
        else:
            self.turn = "O"

    def get_outcome(self):
        board_90 = list(zip(*self.board[::-1]))
        for row, row_90 in zip(self.board, board_90):
            if row == ['X', 'X', 'X'] or row_90 == ['X', 'X', 'X']:
                return "X wins"
            elif row == ['O', 'O', 'O'] or row_90 == ['O', 'O', 'O']:
                return "O wins"
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == ['X', 'X', 'X'] or \
                [board_90[0][0], board_90[1][1], board_90[2][2]] == ['X', 'X', 'X']:
            return "X wins"
        elif [self.board[0][0], self.board[1][1], self.board[2][2]] == ['O', 'O', 'O'] or \
                [board_90[0][0], board_90[1][1], board_90[2][2]] == ['O', 'O', 'O']:
            return "O wins"
        for row in self.board:
            for ij in row:
                if ij == "_":
                    return "Game not finished"
        return "Draw"

    def make_move(self):
        while True:
            try:
                x, y = [int(coor) for coor in input().split()]
                if self.board[x - 1][y - 1] == "_":
                    self.board[x - 1][y - 1] = self.turn
                    if self.turn == "X":
                        self.turn = "O"
                    else:
                        self.turn = "X"
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            except ValueError:
                print("You should enter numbers!")
            except IndexError:
                print("Coordinates should be from 1 to 3!")

    def computer_move(self):
        while True:
            x_y_range = [1, 2, 3]
            x = random.choice(x_y_range)
            y = random.choice(x_y_range)
            if self.board[x - 1][y - 1] == "_":
                self.board[x - 1][y - 1] = self.turn
                if self.turn == "X":
                    self.turn = "O"
                else:
                    self.turn = "X"
                break

    def main(self):
        self.print_board()
        while True:
            self.whose_turn()
            self.make_move()
            self.print_board()
            outcome = self.get_outcome()
            if outcome != "Game not finished":
                break
        print(outcome)


a = TicTacToe()
