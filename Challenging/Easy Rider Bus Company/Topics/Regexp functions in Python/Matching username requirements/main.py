import re

user_name = input()
if re.match('[a-z]', user_name):
    print("Thank you!")
else:
    print("Oops! The username has to start with a letter.")
