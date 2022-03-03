class KnightsTour:
    def __init__(self):
        self.grid_x = None
        self.grid_y = None
        self.board = None
        self.cell_size = None
        self.user_try = None
        self.current_position = None
        self.next_possible_positions = None
        self.move_counter = 2
        self.counter = 0
        self.possible_moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
                               [1, 2], [1, -2], [-1, 2], [-1, -2]]
        self.main()

    def print_board(self):
        borders = " " * len(str(self.grid_y)) + "-" * (self.grid_x * (self.cell_size + 1) + 3)
        print(borders)
        for j in range(self.grid_y):
            row = ""
            for i in self.board[j]:
                row = row + f" {i}"
            if (self.grid_y - j) < 10 and self.grid_y > 9:
                space = " "
                print(f'{space}{self.grid_y - j}|{row} |')
            else:
                space = ""
                print(f'{space}{self.grid_y - j}|{row} |')
        print(borders)
        row_axis = " " * (len(str(self.grid_y)) + 1)
        for i in range(1, self.grid_x + 1, 1):
            if i < 10:
                row_axis = row_axis + (" " * self.cell_size + str(i))
            else:
                row_axis = row_axis + (" " * (self.cell_size - 1) + str(i))
        print(row_axis)

    def board_dimensions(self):
        while True:
            try:
                size = [int(x) for x in input("Enter your board dimensions: ").split()]
                if len(size) != 2:
                    print("Invalid dimensions!")
                elif size[0] < 1 or size[1] < 1:
                    print("Invalid dimensions!")
                else:
                    self.grid_x = size[0]
                    self.grid_y = size[1]
                    self.cell_size = len(str(size[0] * size[1]))
                    self.board = [[("_" * self.cell_size) for _ in range(self.grid_x)] for _ in range(self.grid_y)]
                    break
            except ValueError:
                print("Invalid dimensions!")

    def starting_position(self):
        while True:
            try:
                position = [int(x) for x in input("Enter the knight's starting position: ").split()]
                self.current_position = position
                if len(position) != 2:
                    print("Invalid dimensions!")
                elif position[0] > self.grid_x or position[0] < 1 or position[1] > self.grid_y or position[1] < 1:
                    print("Invalid dimensions!")
                else:
                    symbol = (" " * (self.cell_size - 1)) + "X"
                    self.make_move(position, symbol)
                    break
            except ValueError:
                print("Invalid dimensions!")

    def user_or_sim(self):
        while True:
            self.user_try = input("Do you want to try the puzzle? (y/n): ")
            if self.user_try == "y" or self.user_try == "n":
                break
            print("Invalid input!")

    def make_move(self, move, symbol):
        try:
            if (self.grid_y - move[1]) >= 0 and (move[0] - 1) >= 0:
                self.board[self.grid_y - move[1]][move[0] - 1] = symbol
        except IndexError:
            pass

    def num_possible_moves(self, position):
        moves = []
        for next_possible_move in self.possible_moves:
            x = position[0] + next_possible_move[0]
            y = position[1] + next_possible_move[1]
            if 0 < x < (self.grid_x + 1) and 0 < y < (self.grid_y + 1):
                if self.board[self.grid_y - y][x - 1] == ("_" * self.cell_size):
                    moves.append([x, y])
        return str(len(moves))

    def next_possible_move(self, position, user="y"):
        moves = []
        for next_possible_move in self.possible_moves:
            x = position[0] + next_possible_move[0]
            y = position[1] + next_possible_move[1]
            if 0 < x < (self.grid_x + 1) and 0 < y < (self.grid_y + 1):
                if self.board[self.grid_y - y][x - 1] == ("_" * self.cell_size):
                    moves.append([x, y])
        if user == 'n':
            return moves
        self.next_possible_positions = moves
        for move in moves:
            num = self.num_possible_moves(move)
            symbol = (" " * (self.cell_size - 1)) + num
            self.make_move(move, symbol)

    def make_next_move(self):
        while True:
            try:
                position = [int(x) for x in input("Enter your next move: ").split()]
                if len(position) != 2:
                    print("Invalid dimensions!")
                elif position not in self.next_possible_positions:
                    print("Invalid dimensions!", end='')
                else:
                    self.make_move(self.current_position, (" " * (self.cell_size - 1)) + "*")
                    self.current_position = position
                    self.make_move(position, (" " * (self.cell_size - 1)) + "X")
                    for spot in self.next_possible_positions:
                        if spot != position and self.board[self.grid_y - spot[1]][spot[0] - 1] != (
                                " " * (self.cell_size - 1) + "*"):
                            self.make_move(spot, "_" * self.cell_size)
                    break
            except ValueError:
                print("Invalid dimensions!")

    def warnsdorffs_rule(self, position):
        moves = self.next_possible_move(position, user='n')
        scores = []
        counter = 0
        for col in self.board:
            for element in col:
                if element != ("_" * self.cell_size):
                    counter += 1
        if counter == (self.grid_x * self.grid_y):
            return 1
        elif len(moves) == 0:
            return 0
        else:
            for move in moves:
                scores.append(int(self.num_possible_moves(move)))
            sorted_moves = [move for _, move in sorted(zip(scores, moves))]
            scores.sort()
            if self.move_counter < 10:
                self.make_move(sorted_moves[0], (" " * (self.cell_size - 1)) + str(self.move_counter))
            elif 9 < self.move_counter < 100:
                self.make_move(sorted_moves[0], (" " * (self.cell_size - 2)) + str(self.move_counter))
            else:
                self.make_move(sorted_moves[0], (" " * (self.cell_size - 3)) + str(self.move_counter))
            self.move_counter += 1
            return self.warnsdorffs_rule(sorted_moves[0])

    def results(self):
        count = 0
        for col in self.board:
            for element in col:
                if element == ((" " * (self.cell_size - 1)) + "*") or element == ((" " * (self.cell_size - 1)) + "X"):
                    count += 1
        if count == (self.grid_x * self.grid_y):
            print("What a great tour! Congratulations!")
        else:
            print("No more possible moves!")
            print(f"Your knight visited {count} squares!")

    def main(self):
        self.board_dimensions()
        self.starting_position()
        self.user_or_sim()
        solution = self.warnsdorffs_rule(self.current_position)
        print(solution)
        if self.user_try == 'y' and solution == 1:
            self.board = [[("_" * self.cell_size) for _ in range(self.grid_x)] for _ in range(self.grid_y)]
            while True:
                self.next_possible_move(self.current_position)
                self.print_board()
                if len(self.next_possible_positions) == 0:
                    break
                self.make_next_move()
            self.results()
        elif self.user_try == 'n' and solution == 1:
            print("Here's the solution!")
            for j in range(self.grid_y):
                for i in range(self.grid_x):
                    if self.board[j][i] == ((" " * (self.cell_size - 1)) + "X"):
                        self.board[j][i] = ((" " * (self.cell_size - 1)) + "1")
            self.print_board()
        else:
            print("No solution exists!")


a = KnightsTour()
