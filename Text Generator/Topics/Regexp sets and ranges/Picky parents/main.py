import re

# your code here
name = input()
if re.match(r'[B-N][aeiou]', name) is not None:
    print("Suitable!")
