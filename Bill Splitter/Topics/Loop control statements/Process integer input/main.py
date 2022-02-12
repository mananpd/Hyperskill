# put your python code here
numbers = []
while True:
    x = int(input())
    if x < 10:
        continue
    elif x > 100:
        break
    else:
        numbers.append(x)
for num in numbers:
    print(num)
