""" Lesson 6 ex.1 """


class EvenIterator():
    """ Iterator that retrieves all items on even indexes from the list. """

    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.ind = -2
        self.stop = len(self.iter_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind <= self.stop - 2:
            self.ind += 2
            return self.iter_list[self.ind]
        raise StopIteration


def _test():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    for item in EvenIterator(my_list):
        print(item)


_test()
