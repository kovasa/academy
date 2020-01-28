def difference_lists(list1=[], list2=[]):
    if not list1:
        list1 = input("Input list1: ").split()
    if not list2:
        list2 = input("Input list2: ").split()

    #return list(set(list1).symmetric_difference(set(list2))) # если не важен порядок и нет повторяющихся элементов

    list_merging = list1 + list2
    list_intersection = list(set(list1).intersection(set(list2)))
    list_result = []
    for item in list_merging:
        if item not in list_intersection:
            list_result.append(item)

    return list_result

def test1_10():
    print(difference_lists(['abc', 'dfh','abc', 'wer'],
                           ['dfh', 'ara', 'wer','wer']))
#     print(difference_lists())

test1_10()
