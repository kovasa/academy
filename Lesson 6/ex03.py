""" Lesson 6 ex.3 """


def gen_dict(list_key, list_val):
    """ Generates a dictionary from a list of keys and a list of values. """
    max_val = len(list_val)
    return [{k: list_val[ind] if max_val > ind else None}
            for ind, k in enumerate(list_key)]


def _test():
    print(gen_dict([1, 2, 3, 4, 5], [1, 4, 9]))
    print(gen_dict([1, 2], [1, 4, 9]))


_test()
