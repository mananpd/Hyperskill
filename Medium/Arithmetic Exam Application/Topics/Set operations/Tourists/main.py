# work with these variables
eugene = set(input().split())
rose = set(input().split())

print(eugene.difference(rose) | rose.difference(eugene))
