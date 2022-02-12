# put your python code here
values = []
squared_values = []
while True:
    x = int(input())
    values.append(x)
    squared_values.append(x ** 2)
    if sum(values) == 0:
        break
print(sum(squared_values))
