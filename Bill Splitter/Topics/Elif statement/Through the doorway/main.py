A = float(input())
B = float(input())
C = float(input())
X = float(input())
Y = float(input())

if (A <= X) and (B <= Y or C <= Y):
    print("The box can be carried")
elif (B <= X) and (A <= Y or C <= Y):
    print("The box can be carried")
elif (C <= X) and (B <= Y or A <= Y):
    print("The box can be carried")
elif (A <= Y) and (B <= X or C <= X):
    print("The box can be carried")
elif (B <= Y) and (A <= X or C <= X):
    print("The box can be carried")
elif (C <= Y) and (A <= X or B <= X):
    print("The box can be carried")
else:
    print("The box cannot be carried")
