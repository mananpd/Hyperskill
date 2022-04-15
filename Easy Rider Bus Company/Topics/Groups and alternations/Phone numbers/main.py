import re

string = input()
# your code here
pattern = r'\+([\d])[\s-]?([\d]{3})[\s-]?([\d]{3}[\s-]?[\d]{2}[\s-]?[\d]{2})'
match = re.match(pattern, string)
if match:
    phone_tuple = match.groups()
    print(f'Full number: {string}')
    print(f'Country code: {phone_tuple[0]}')
    print(f'Area code: {phone_tuple[1]}')
    print(f'Number: {phone_tuple[2]}')
else:
    print('No match')
