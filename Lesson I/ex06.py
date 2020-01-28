def new_dict(n=None):
    if n is None:
        n = int(input("Input integer number: "))
    dic = {}
    for i in range(1, n+1):
        dic[i] = i*i
    print(dic)

def test1_6():
    new_dict(5)
    new_dict(0)
    new_dict(1)
#     new_dict()
    
test1_6()
