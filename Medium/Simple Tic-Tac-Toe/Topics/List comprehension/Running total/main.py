a = input()
b = [int(x) for x in a]
cum_sum = 0
c = []
for x in b:
    cum_sum += x
    c.append(cum_sum)
print(c)
