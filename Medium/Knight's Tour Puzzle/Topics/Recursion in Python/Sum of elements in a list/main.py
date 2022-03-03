def list_sum(some_list):
    if not some_list:
        return 0
    # base case
    elif len(some_list) == 1:
        return some_list[0]
    # recursive case
    else:
        return some_list[0] + list_sum(some_list[1:])
