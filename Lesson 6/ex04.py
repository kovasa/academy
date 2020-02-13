""" Lesson 6 ex.4 """


def cycle(obj):
    """ Generator that returns a cyclic iterator. """
    while True:
        for item in obj:
            yield item


def _test():
    my_iter = cycle([1, 2, 3])
    count = 0
    for item in my_iter:
        print(item, end=' ')
        count += 1
        if count == 20:
            break


_test()
