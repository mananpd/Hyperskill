import sys

# write your code here
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)
sys.setrecursionlimit(200)
new_limit = sys.getrecursionlimit()
print(new_limit)
