iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    kwargs_dic = {'species': species,
                  'petal_length': petal_length,
                  'petal_width': petal_width}
    for key, value in kwargs.items():
        kwargs_dic.update({key: value})

    iris.update({id_n: kwargs_dic})
