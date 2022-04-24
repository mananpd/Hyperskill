import re

string = input()
# your code here
if re.match("Good morning", string):
    print("Good morning")
elif re.match("Good afternoon", string):
    print("Good afternoon")
elif re.match("Good evening", string):
    print("Good evening")
else:
    print("No greeting!")
