def remove_dupl(list1=[]):
    if not list1:
        list1 = input("Input list: ").split()
        
    #return list(set(list1)) # если не важен порядок

    new_list = []
    for val in list1:
        if val not in new_list:
            new_list.append(val)

    return new_list
            
def test1_9():
    print(remove_dupl(['abc', 'dfh', 'abc', 'wer']))
#     print(remove_dupl())
    
test1_9()
