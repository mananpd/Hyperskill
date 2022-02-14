from string import ascii_lowercase
single = [letter for letter in ascii_lowercase]
double = [letter * 2 for letter in single]
double_alphabet = {single[i]: double[i] for i in range(len(single))}
