# write your code here
import operator
import random


def question_level():
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    try:
        answer = int(input())
        if answer == 1 or answer == 2:
            return answer
        else:
            print("Incorrect format.")
    except ValueError:
        print("Incorrect format.")


def input_answer():
    try:
        answer = int(input())
        return answer
    except ValueError:
        print("Wrong format! Try again.")


def calculator(num1, oper, num2):
    num1, num2 = int(num1), int(num2)
    return ops[oper](num1, num2)


def level_1_problem():
    problem = f"{random.randint(2, 9)} {random.sample(ops.keys(), 1)[0]} {random.randint(2, 9)}"
    print(problem)
    op1, oper, op2 = problem.split()
    while True:
        user_answer = input_answer()
        if type(user_answer) == int:
            break
    if user_answer == calculator(op1, oper, op2):
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def level_2_problem():
    problem = random.randint(11, 29)
    print(problem)
    while True:
        user_answer = input_answer()
        if type(user_answer) == int:
            break
    if user_answer == (problem ** 2):
        print("Right!")
        return 1
    else:
        print("Wrong!")
        return 0


def save_results(level, num_of_right_answers):
    save_answer = input()
    if save_answer.lower() == 'yes' or save_answer == 'y':
        name = input("What is your name?")
        with open("results.txt", "a") as file:
            if level == 1:
                file.write(f"{name}: {num_of_right_answers}/5 in level {level} (simple operations with numbers 2-9).")
            elif level == 2:
                file.write(f"{name}: {num_of_right_answers}/5 in level {level} (integral squares of 11-29).")
        print('The results are saved in "results.txt".')
        exit()
    else:
        exit()


ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul}

num_of_questions = 5
num_of_right = 0

while True:
    level_answer = question_level()
    if level_answer == 1 or level_answer == 2:
        break
for _ in range(num_of_questions):
    if level_answer == 1:
        num_of_right += level_1_problem()
    elif level_answer == 2:
        num_of_right += level_2_problem()
print(f"Your mark is {num_of_right}/5. Would you like to save the result? Enter yes or no.")
save_results(level_answer, num_of_right)
