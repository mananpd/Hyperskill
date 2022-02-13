# write your code here
def is_one_digit(v):
    if v.is_integer() and -10 < v < 10:
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 in "+-*"):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


memory = 0
while True:
    print("Enter an equation")
    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue
    if oper not in ['+', '-', "*", "/"]:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue
    else:
        check(x, y, oper)
        if oper == "+":
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/' and y != 0:
            result = x / y
        else:
            print("Yeah... division by zero. Smart move...")
            continue

    print(result)

    while True:
        print("Do you want to store the result? (y / n):")
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                msg_dic = {"msg_10": "Are you sure? It is only one digit! (y / n)",
                           "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
                           "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)"}
                while True:
                    message = "msg_" + str(msg_index)
                    print(msg_dic[message])
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer != "n":
                        continue
                    elif answer == "n":
                        break
            else:
                memory = result
                break
            break
        elif answer == "n":
            break

    while True:
        print("Do you want to continue calculations? (y / n):")
        answer = input()
        if answer == "y":
            break
        elif answer != "n":
            continue
        else:
            break
    if answer == "y":
        continue
    elif answer == "n":
        break
