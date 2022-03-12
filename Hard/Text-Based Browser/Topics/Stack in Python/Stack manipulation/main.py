import collections

length = int(input())
d = collections.deque()

for _ in range(length):
    operation_element = input().split(" ")
    if len(operation_element) > 1:
        operation = operation_element[0]
        element = operation_element[1]
    else:
        operation = operation_element[0]
    if operation == "PUSH":
        d.append(element)
    elif operation == "POP":
        d.pop()

for _ in range(len(d)):
    print(d.pop())
