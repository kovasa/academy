def merge_dicts(dict1, dict2):
    new_dict = {}
    new_dict.update(dict1)
    new_dict.update(dict2)

    return new_dict

def test1_7():
    print(merge_dicts({1: 'one', 2: 'two', 3: 'three'}, 
                      {4: 'four', 5: 'five'}))
    print(merge_dicts({1: 'one', 2: 'two', 3: 'three'}, 
                      {2: 'new_two', 4: 'four', 5: 'five'}))

test1_7()
