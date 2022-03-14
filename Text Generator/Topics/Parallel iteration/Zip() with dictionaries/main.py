# please do not modify the following code
_d_list = [keyword.split(':') for keyword in input().split(', ')]
domestic_animal = {key: value for key, value in _d_list}
_w_list = [keyword.split(':') for keyword in input().split(', ')]
wild_animal = {key: value for key, value in _w_list}

# your code here
zipped = zip(domestic_animal.items(), wild_animal.items())
for (domestic_key, domestic_value), (wild_key, wild_value) in zipped:
    print(f"The domestic animal's {domestic_key} is '{domestic_value}'.")
    print(f"The wild animal's {wild_key} is '{wild_value}'.")
