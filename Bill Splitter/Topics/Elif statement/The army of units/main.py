army = int(input())
if army < 1:
    print("no army")
if 1 <= army <= 9:
    print("few")
if 10 <= army <= 49:
    print("pack")
if 50 <= army <= 499:
    print("horde")
if 500 <= army <= 999:
    print("swarm")
if army >= 1000:
    print("legion")
