def two_sym(S=""):
    if not S:
        S = input("Input string: ")
    if len(S) < 2:
        return 'Empty String'
    else:
        return S[:2] + S[-2:]

def test1_3():
    print(two_sym('w3resource'))
    print(two_sym('w3'))
    print(two_sym('w'))
#     print(two_sym())

test1_3()
