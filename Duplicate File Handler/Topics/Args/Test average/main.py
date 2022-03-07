def average_mark(*test):
    total = 0
    for n in test:
        total += n
    return round(total/len(test), 1)
