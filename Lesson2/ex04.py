def my_range(start=0, stop=0, step=1):
    list1 = []
    k = start
    while k < stop:
        list1.append(k)
        k += step
    return list1

def test2_4():
    print(my_range(0, 5))
    print(my_range(stop=5))
    print(my_range(2, 10, 2))

test2_4()
