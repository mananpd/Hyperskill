class Calculator:
    def __init__(self):
        self.numbers = []
        self.operators = []
        self.not_exit = True
        self.answer = None
        self.menu()

    def user_input(self):
        user_input = input()
        if user_input.startswith("/"):
            if user_input == "/exit":
                print("Bye!")
                self.not_exit = False
                return False
            elif user_input == '/help':
                print("The program calculates the sum of numbers")
                return False
            else:
                print("Unknown command")
        else:
            try:
                user_input = user_input.split()
                self.numbers = [int(user_input[i]) for i in range(0, len(user_input), 2)]
                self.operators = [user_input[i] for i in range(1, len(user_input), 2)]
                return True
            except ValueError:
                print("Invalid expression")

    def operators_reduction(self):
        for i in range(len(self.operators)):
            if len(self.operators[i]) * "+" == self.operators[i]:
                self.operators[i] = "+"
            elif len(self.operators[i]) * "-" == self.operators[i]:
                if len(self.operators[i]) % 2 == 0:
                    self.operators[i] = "+"
                else:
                    self.operators[i] = "-"
            else:
                print("error")
                return False
        return True

    def addition(self, num1, num2):
        self.answer = num1 + num2

    def subtraction(self, num1, num2):
        self.answer = num1 - num2

    def menu(self):
        while self.not_exit:
            if self.user_input():
                if self.operators_reduction():
                    if len(self.numbers) > 0:
                        self.answer = 0
                        self.addition(self.answer, self.numbers.pop(0))
                        for i in range(len(self.operators)):
                            if self.operators[i] == "+":
                                self.addition(self.answer, self.numbers.pop(0))
                            elif self.operators[i] == "-":
                                self.subtraction(self.answer, self.numbers.pop(0))
                if self.answer is not None:
                    print(self.answer)


a = Calculator()
