import sys
sys.setrecursionlimit(10000)


def single_char_regex(regex_char, input_char):
    return True if regex_char in '. ' or regex_char == input_char else False


def equal_string_regex(regex_string, input_string):
    if regex_string == "":
        return True
    elif regex_string == "$" and input_string == "":
        return True
    elif len(regex_string) > 1 and regex_string[1] == "." and regex_string[0] == "\\":
        return equal_string_regex(regex_string[2:], input_string[1:])
    elif len(regex_string) > 1 and regex_string[0] == "\\":
        return equal_string_regex(regex_string[1:], input_string)
    elif len(regex_string) > 1 and regex_string[1] == "?":
        if not single_char_regex(regex_string[0], input_string[0]):
            return equal_string_regex(regex_string[2:], input_string)
        else:
            return equal_string_regex(regex_string[2:], input_string[1:])
    elif len(regex_string) > 1 and regex_string[1] == "*":
        if input_string == "":
            return True
        if not single_char_regex(regex_string[0], input_string[0]):
            return equal_string_regex(regex_string[2:], input_string)
        else:
            return equal_string_regex(regex_string, input_string[1:])
    elif len(regex_string) > 1 and regex_string[1] == "+":
        if regex_string[0] == ".":
            regex_string = input_string[0] + regex_string[1:]
        if len(input_string) > 1 and single_char_regex(regex_string[0], input_string[1]):
            return equal_string_regex(regex_string, input_string[1:])
        elif single_char_regex(regex_string[0], input_string[0]):
            return equal_string_regex(regex_string[2:], input_string[1:])
        else:
            return False
    elif input_string == "" or not single_char_regex(regex_string[0], input_string[0]):
        return False
    else:
        return equal_string_regex(regex_string[1:], input_string[1:])


def different_string_regex(regex_string, input_string):
    if regex_string.startswith("^"):
        return equal_string_regex(regex_string[1:], input_string)
    elif equal_string_regex(regex_string, input_string):
        return True
    elif input_string == "":
        return False
    else:
        return different_string_regex(regex_string, input_string[1:])


reg, inp = input().split("|")
print(different_string_regex(reg, inp))

