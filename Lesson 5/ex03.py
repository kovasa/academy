""" Lesson 5 ex.3 """


class Observable():
    """ Saves kwargs as class attributes and prints only public attributes. """

    def __init__(self, **kwargs):
        self.attr = kwargs

    def __str__(self):
        attrs = [(f"{k}={self.__getattr__(k)}") for k, v in self.attr.items()
                 if not k.startswith('_')]
        str_r = f"{self.__class__.__name__}({', '.join(attrs)})"
        return str_r

    def __getattr__(self, name):
        value = self.attr[name]
        return f"\'{value}\'" if isinstance(value, str) else value


def _test():
    class XYZ(Observable):  # pylint: disable=too-few-public-methods
        """ Test class. """

    xyz = XYZ(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
    print(xyz)
    print(xyz.foo)
    print(xyz.name)
    print(xyz._bazz)  # pylint: disable=protected-access


_test()
