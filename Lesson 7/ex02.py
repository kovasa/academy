""" Lesson 7 ex.2 """


from time import perf_counter, sleep


def decor_time(fun):
    """ Decorator computes and prints working time of given class method. """
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        res = fun(*args, **kwargs)
        print(f'Время работы метода {fun.__name__}: \
{(perf_counter()-time_start)*1000} мс.')
        return res
    return wrapper


def time_methods(*args):
    """ Calls decorator. """
    def decor(cls):
        """ Decorator of the given class that calls 'decor_time' decorator. """
        for meth in dir(cls):
            if meth in args:
                setattr(cls, meth, decor_time(getattr(cls, meth)))
        return cls
    return decor


def _test():
    @time_methods('inspect', 'finalize')
    class Spam:
        """ Class for test. """
        def __init__(self, sec):
            self.sec = sec

        def inspect(self):
            """ Test func 1. """
            sleep(self.sec)

        def blanc(self):
            """ Test func 2. """
            return self.sec

    spam = Spam(5)
    spam.inspect()  # должно вывести сообщение о времени работы
    spam.blanc()  # ничего не выводить


_test()
