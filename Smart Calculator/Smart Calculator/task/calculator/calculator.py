class Calculator:
    def __init__(self):
        self.numbers = []
        self.operators = []
        self.not_exit = True
        self.answer = None
        self.variables = {}
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
        elif "=" in user_input:
            user_input = [char.strip(" ") for char in user_input.split("=")]
            if user_input[0].isalpha():
                if user_input[1].isalpha():
                    if user_input[1] in self.variables:
                        self.variables[user_input[0]] = self.variables[user_input[1]]
                    else:
                        print("Unknown variable")
                elif user_input[1].isdigit():
                    self.variables[user_input[0]] = int(user_input[1])
                else:
                    print("Invalid assignment")
            else:
                print("Invalid identifier")
        elif len(user_input.split()) == 1:
            if user_input in self.variables:
                print(self.variables[user_input])
            else:
                print("Unknown variable")
        else:
            try:
                user_input = user_input.split()
                self.numbers = [user_input[i] for i in range(0, len(user_input), 2)]
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
        if num2.isalpha():
            num2 = self.variables[num2]
        self.answer = int(num1) + int(num2)

    def subtraction(self, num1, num2):
        if num2.isalpha():
            num2 = self.variables[num2]
        self.answer = int(num1) - int(num2)

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
