def compare_sets(set1, set2, set3):
    return set3 <= set1 and set3 <= set2

def test1_5():
    print(compare_sets(set([1,2]), set([2,3]), set([2])))
    print(compare_sets(set([1,2]), set([3,4]), set([5])))
    print(compare_sets(set([1,2]), set([3,4]), set([1])))
    print(compare_sets(set([1,2]), set([3,4]), set([3])))
    print(compare_sets(set([1,2,3]), set([2,3,4]), set([2,3])))
    
test1_5()
