""" Lesson 7 ex.1 """


from time import perf_counter, sleep


def average_time(num):
    """ Calls decorator. """
    list_time = []

    def gen_calls(func):
        """
        Decorator computes the average working time of last 'num' times.
        """
        def wrapper(sec):
            nonlocal num

            time_start = perf_counter()
            res = func(sec)
            list_time.append((perf_counter()-time_start)*1000)
            count_cal = len(list_time)
            count = count_cal if num > count_cal else num
            mid_val = sum(list_time[count_cal - count:])
            print(f'Среднее время работы: {int(mid_val/count)} мс.')

            return res
        return wrapper
    return gen_calls


def _test():

    @average_time(num=2)
    def foo_sleep(sec):
        sleep(sec)
        return sec

    foo_sleep(3)
    foo_sleep(7)
    foo_sleep(1)


_test()
