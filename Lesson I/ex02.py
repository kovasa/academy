def count_sym(S=""):
    if not S:
        S = input("Input line: ")
        if not S:
            print("Error: length of line must be > 0")
            return

    result = {}
    for sym in S:
        if sym not in result:
            result[sym] = S.count(sym)

    print(result)

def test1_2():
    count_sym('string consists')
    count_sym('122333444455555')
#     count_sym()
    
test1_2()
