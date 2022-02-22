def xor(a, b):
    if a and b:
        return False
    elif bool(a) is False and bool(b) is False:
        return False
    else:
        return a or b
