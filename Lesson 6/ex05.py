""" Lesson 6 ex.5 """


def chain(*args):
    """ Generator that iterates the passed objects. """
    for item in args:
        for iter_i in item:
            yield iter_i


def _test():
    my_iter = chain([1, 2, 3], "hello", {'a': 'A', 'b': 'B'})
    for item in my_iter:
        print(item)


_test()
