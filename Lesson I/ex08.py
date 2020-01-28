def dict_max(dic={}):
    if not dic:
        return []

    list_highest = []
    list_values = list(dic.values())
    list_values.sort()
    for i in range(3):
        if list_values:
            list_highest.append(list_values.pop())
    return list_highest

def test1_8():
    print(dict_max({1: 1, 5: 25, 3: 9, 2: 4, 4: 16}))
    print(dict_max({3: 9, 2: 4, 4: 16}))
    print(dict_max(None))
    print(dict_max())

test1_8()
