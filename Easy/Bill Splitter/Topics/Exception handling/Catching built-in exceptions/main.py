def exception_check(a, b):
    try:
        results = a/b
    except ZeroDivisionError:
        print("The Error!")
    else:
        print(results)
