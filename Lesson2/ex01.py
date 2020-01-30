def sq(x=None):
    if x is None:
        x = int(input("Input finish of interval: "))

    k = 0
    for i in range(1, x+1, 2):
        print(i*i, end = " ")
        k += 1

    print('\nCount = ', k)



def test2_1():
    sq(5)
    sq(1)
    sq(10)
#     sq()

test2_1()
