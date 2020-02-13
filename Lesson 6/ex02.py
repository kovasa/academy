""" Lesson 6 ex.2 """


def gen_atr(obj):
    """ Generates a list of all public attributes of an object. """
    for item in dir(obj):
        if not item.startswith('__'):
            yield item


def _test():
    xyz = gen_atr("string")
    print(next(xyz))
    print(next(xyz))

    for item in xyz:
        print(item)


_test()
