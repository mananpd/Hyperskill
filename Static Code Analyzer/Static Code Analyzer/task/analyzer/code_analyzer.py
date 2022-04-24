import re


def insert_error(error, num, error_dic):
    if num in error_dic:
        error_dic[num].append(error)
    else:
        error_dic[num] = [error]


def S001(script, error_dic: dict):
    error = "S001"
    for num, line in enumerate(open(script, 'r'), start=1):
        if len(line) > 79:
            insert_error(error, num, error_dic)


def S002(script, error_dic: dict):
    error = "S002"
    for num, line in enumerate(open(script, 'r'), start=1):
        if line.startswith(" "):
            match = re.search(" +", line)
            if (match.span()[1]) % 4 != 0:
                insert_error(error, num, error_dic)


def S003(script, error_dic: dict):
    error = "S003"
    for num, line in enumerate(open(script, 'r'), start=1):
        line = line.strip()
        if line.endswith(";") and "#" not in line:
            insert_error(error, num, error_dic)
        elif "#" in line and not line.startswith("#"):
            line_command = line.split("#")[0]
            if line_command.strip().endswith(";"):
                insert_error(error, num, error_dic)


def S004(script, error_dic: dict):
    error = "S004"
    for num, line in enumerate(open(script, 'r'), start=1):
        index = line.find("#")
        if index != -1 and index != 0:
            index -= 2
            if line[index: index + 2] != "  ":
                insert_error(error, num, error_dic)


def S005(script, error_dic: dict):
    error = "S005"
    for num, line in enumerate(open(script, 'r'), start=1):
        index = line.find("#")
        if index > -1:
            comments = line[(index + 1):]
            if re.search("todo", comments, flags=re.I):
                insert_error(error, num, error_dic)


def S006(script, error_dic: dict):
    error = "S006"
    count = 0
    for num, line in enumerate(open(script, 'r'), start=1):
        if line == "\n":
            count += 1
        else:
            if count > 2:
                insert_error(error, num, error_dic)
            count = 0


def print_message(error_dic: dict):
    for num, item in error_dic.items():
        for error in item:
            print(f"Line {num}: ", end="")
            if error == "S001":
                print("S001 Too long")
            if error == "S002":
                print("S002 Indentation is not a multiple of four")
            if error == "S003":
                print("S003 Unnecessary semicolon")
            if error == "S004":
                print("S004 At least two spaces required before inline comments")
            if error == "S005":
                print("S005 TODO found")
            if error == "S006":
                print("S006 More than two blank lines used before this line")


file_name = input()
errors = {}
S001(file_name, errors)
S002(file_name, errors)
S003(file_name, errors)
S004(file_name, errors)
S005(file_name, errors)
S006(file_name, errors)
print_message(dict(sorted(errors.items())))
