def func_count(a:int, b:int, c):
    if c == 0:
        print("Error: you can't divide by 0")
        return

    k = 0
    for i in range(a+1, b):
        if i%c == 0:
            k += 1

    print('Count = ',k)

def test2_2():
    func_count(0, 5, 2)

test2_2()
