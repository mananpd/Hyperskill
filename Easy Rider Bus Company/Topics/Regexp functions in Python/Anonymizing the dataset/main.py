import re

string = input()
# your code
string = re.sub('@(\w+)', "<AUTHOR>", string, count=1)
string = re.sub('@(\w+)', "<HANDLE>", string)
print(string)
