import re

template = r'are you ready??.?.?'
a = re.match(template, input())
if a:
    print(a.end())
else:
    print(0)
