import gc


def prod_sum_list(*args, **kwargs):
    s, p = 0, 1


    # def is_rec(obj):
    #     # my_obj = obj
    #     gc.set_debug(gc.DEBUG_SAVEALL)
    #     gc.get_count()
    #     list_id = id(obj)
    #     del obj
    #     gc.collect()
    #     for item in gc.garbage:
    #         if list_id == id(item):
    #             print("Error: circular reference: ")
    #             return True
    #     return False


    def get_item(obj):
        nonlocal s
        nonlocal p
        if isinstance(obj, dict):
            for value in obj.values():
                get_item(value)
        elif isinstance(obj, list) or isinstance(obj, tuple):
            # if is_rec(obj):
            #     return None
            for item in obj:
                get_item(item)
        elif obj != 0:
            s += obj
            p *= obj

    get_item(args)
    get_item(kwargs)

    return s, p


def test():
    print(prod_sum_list(1, 2, [3, 4, (5, 6, 0)], a=(10, 11),
                        b=(3, 4, [5, 6, [7, 8], []])))
    # a = [10, 11, [12]]
    # a.append(a)
    # print(prod_sum_list(1, 2, [3, 4, (5, 6, 0)], a,
    #                     b=(3, 4, [5, 6, [7, 8], []])))


test()
