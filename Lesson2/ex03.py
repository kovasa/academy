def fact(x=None):
    if x is None:
        x = int(input("Input integer: "))

    f = 1
    for i in range(1, x+1):
        f *= i

    return f



def test2_3():
    print(fact(2))
    print(fact(5))
    print(fact())

test2_3()
