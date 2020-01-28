def count_strings(S=[]):
    if not S:
        S = input("Input strings: ").split()
    k = 0
    for item in S:
        if len(item) >= 2 and item[0] == item[-1:]:
            k += 1
    return k    

def test1_4():
    print(count_strings(['a', 'xz', 'aa', 'abba', 'ara', '1aa2']))
#     print(count_strings())
    
test1_4()
