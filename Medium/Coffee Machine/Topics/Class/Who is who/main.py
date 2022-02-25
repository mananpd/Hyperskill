class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


angel = Angel()
demon = Demon()
for x in [angel, demon]:
    print(x.color)
    print(x.feature)
    print(x.home)
