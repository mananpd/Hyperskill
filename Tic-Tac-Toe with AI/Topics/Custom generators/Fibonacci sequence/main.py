def fibonacci(n):
    value = []
    for i in range(n):
        if i == 0:
            value.append(0)
        elif i == 1:
            value.append(1)
        else:
            value.append(value[i - 1] + value[i - 2])
        yield value[i]
