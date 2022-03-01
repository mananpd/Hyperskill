numbers = [int(x) for x in input()]
running_mean = []
for i in range(0, len(numbers) - 1):
    running_mean.append((numbers[i] + numbers[i+1])/2)
print(running_mean)
