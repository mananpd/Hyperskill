# write your code here
for i in range(1, 11):
    with open("file" + str(i) + ".txt", "w") as f:
        f.write(str(i))
