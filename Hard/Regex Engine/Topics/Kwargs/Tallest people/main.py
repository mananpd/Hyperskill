def tallest_people(**kwargs):
    tallest = {}
    max_height = 0
    for name, height in kwargs.items():
        if height > max_height:
            max_height = height
            tallest = {name: height}
        elif height == max_height:
            tallest.update({name: height})
    for name, height in sorted(tallest.items()):
        print(name, ":", height)
