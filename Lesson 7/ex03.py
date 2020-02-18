""" Lesson 7 ex.3 """


def carry(func):
    """ Decorator converts call of function with defined number of
    positional arguments to call of function with one argument. """

    def wrapper(*args):
        if len(args) == func.__code__.co_argcount:
            return func(*args)
        return lambda x: wrapper(*(args+(x,)))

    return wrapper


def _test():
    @carry
    def foo1(aaa, bbb, ccc, ddd):
        return aaa + bbb + ccc + ddd

    @carry
    def foo2(aaa, bbb):
        return aaa * bbb

    print(foo1(1)(5)(7)(2))  # pylint: disable=no-value-for-parameter
    print(foo2(10)(5))  # pylint: disable=no-value-for-parameter


_test()
