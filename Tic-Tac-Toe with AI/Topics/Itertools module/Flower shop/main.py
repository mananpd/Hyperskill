import itertools

for item in itertools.chain(itertools.combinations(flower_names, 1),
                            itertools.combinations(flower_names, 2),
                            itertools.combinations(flower_names, 3)):
    print(item)
