class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = 0

    def calculate_area(self):
        # calculate the area here
        self.area = 0.5 * self.a * self.b

    def is_right(hyp, leg_1, leg_2):
        return hyp ** 2 == (leg_1 ** 2) + (leg_2 ** 2)

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if RightTriangle.is_right(input_c, input_a, input_b):
    a = RightTriangle(input_c, input_a, input_b)
    a.calculate_area()
    print(round(a.area, 1))
else:
    print("Not right")
