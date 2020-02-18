""" Lesson 7 ex.4 """


def carry(func):
    """ Decorator checks types of arguments according to annotations. """

    def wrapper(*args, **kwargs):
        ind = 0
        for name, typ in func.__annotations__.items():
            if name == 'return':
                continue

            if typ is None:
                raise ValueError(f'Не задан тип аргумента {name}')

            item = kwargs[name] if kwargs.get(name) else args[ind]
            ind += 1
            if not isinstance(item, typ):
                raise ValueError(f'Тип аргумента {name} не '
                                 f'соответствует типу в аннотации {typ}')
            return func(*args, **kwargs)

    return wrapper


def _test():
    @carry
    def func(num: int, output: list) -> list:
        return num * output

    func(2, output=['a', 'b'])
    func('2', output=['a', 'b'])


_test()
