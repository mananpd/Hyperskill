import re

string = input()
regex = r'\$\d+'
match = re.match(regex, string)
if match:
    print('Amount found:', string)
else:
    print('No match!')
