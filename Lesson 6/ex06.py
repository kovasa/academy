""" Lesson 6 ex.6 """


def check_div(line):
    """ Performs integer division of values in pairs
        and prints result or exception.
    """
    new_list = [x.split() for x in line.split('\n')]
    for count in range(int(new_list[0][0])):
        try:
            print(int(new_list[count+1][0]) // int(new_list[count+1][1]))
        except (ZeroDivisionError, ValueError) as exc:
            print("Error Code:", exc)


def _test():
    check_div("""3
1 0
2 $
3 1
""")


_test()
