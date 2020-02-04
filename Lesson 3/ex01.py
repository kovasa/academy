def square_list(my_list=''):
    return list(map(lambda x: x**2, my_list))


def even_pos(my_list=''):
    new_list = []
    for i, item in enumerate(my_list):
        if i % 2 != 0:
            new_list.append(item)
    return new_list


def cube_list(my_list=''):
    new_list = []
    for i, item in enumerate(my_list):
        if i % 2 == 0 and item % 2 == 0:
            new_list.append(item**3)
    return new_list


def test():
    print(square_list((1, 2, 3)))
    print(square_list([4, 5, 6]))
    print(square_list())

    print(even_pos((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
    print(even_pos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(even_pos())

    print(cube_list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
    print(cube_list([2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(cube_list())


test()
