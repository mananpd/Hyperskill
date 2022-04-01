from collections import deque
import re


class Calculator:
    def __init__(self):
        self.postfix = []
        self.my_stack = deque()
        self.precedence = {'-': 1, '+': 1, '*': 2, '/': 2}
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
        elif user_input.strip(" ").isalpha():
            if user_input.strip(" ") in self.variables:
                print(self.variables[user_input.strip(" ")])
            else:
                print("Unknown variable")
        elif user_input.isdigit():
            print(user_input)
        else:
            try:
                user_input = re.sub(r'([+])\1+', r'\1', user_input)
                user_input = re.findall('[+-/*]|[0-9]+|[a-z]+|[)(]', user_input)
                while len(user_input) > 0:
                    if user_input[0].isalpha() or user_input[0].isdigit():
                        self.postfix.append(user_input[0])
                        del user_input[0]
                    elif len(self.my_stack) == 0 or self.my_stack[len(self.my_stack) - 1] == "(":
                        self.my_stack.append(user_input[0])
                        del user_input[0]
                    elif user_input[0] in self.precedence and self.precedence.get(user_input[0]) > self.precedence.get(self.my_stack[len(self.my_stack) - 1]):
                        self.my_stack.append(user_input[0])
                        del user_input[0]
                    elif user_input[0] in self.precedence and self.precedence.get(user_input[0]) <= self.precedence.get(self.my_stack[len(self.my_stack) - 1]):
                        while True:
                            self.postfix.append(self.my_stack.pop())
                            if len(self.my_stack) == 0:
                                break
                            if self.my_stack[len(self.my_stack) - 1] == "(":
                                break
                            elif self.my_stack[len(self.my_stack) - 1] == "+":
                                break
                            elif self.my_stack[len(self.my_stack) - 1] == "-":
                                break
                        self.my_stack.append(user_input[0])
                        del user_input[0]
                    elif user_input[0] == "(":
                        self.my_stack.append(user_input[0])
                        del user_input[0]
                    elif user_input[0] == ")":
                        while True:
                            self.postfix.append(self.my_stack.pop())
                            if self.my_stack[len(self.my_stack) - 1] == "(":
                                self.my_stack.pop()
                                break
                        del user_input[0]
                while True:
                    if len(self.my_stack) == 0:
                        break
                    self.postfix.append(self.my_stack.pop())
                return True
            except ValueError:
                print("Invalid expression")
            except IndexError:
                print("Invalid expression")

    def calculation(self):
        for element in self.postfix:
            try:
                if element.isdigit():
                    self.my_stack.append(int(element))
                elif element.isalpha():
                    if element in self.variables:
                        self.my_stack.append(self.variables[element])
                    # else:
                    #     print("Unknown variable")
                else:
                    num2 = self.my_stack.pop()
                    num1 = self.my_stack.pop()
                    if element == "+":
                        ans = num1 + num2
                    elif element == "-":
                        ans = num1 - num2
                    elif element == "*":
                        ans = num1 * num2
                    elif element == "/":
                        ans = num1 / num2
                    self.my_stack.append(ans)
            except IndexError:
                print("Invalid expression")

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
                self.calculation()
                if len(self.my_stack) != 0:
                    print(int(self.my_stack.pop()))
                    self.postfix = []
                    self.my_stack = deque()


a = Calculator()
