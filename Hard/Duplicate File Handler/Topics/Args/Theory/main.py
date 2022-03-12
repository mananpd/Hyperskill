#  You can experiment here, it won’t be checked
def average_mark(*test):
    total = 0
    for n in test:
        total += n
    return total/len(test)

