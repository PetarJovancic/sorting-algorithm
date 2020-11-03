"""
Function for sorting gender then lastname ascending
"""
def gender_lastname_sort(final_list):
    l=len(final_list)
    if l <=1:
        return final_list
    else:
        pivot=final_list.pop()
    items_greater=[]
    items_lower = []
    sub_items_lower=[]
    sub_items_greater=[]
    sub_items_lower2 = []
    sub_items_greater2 = []
    for item in final_list:
        if item[2]>pivot[2]:
            items_greater.append(item)
        else:
            items_lower.append(item)
    pivot2 = items_greater.pop()
    pivot3 = items_lower.pop()
    for item2 in items_greater:
        if item2[0] > pivot2[0]:
            sub_items_greater.append(item2)
        else:
            sub_items_lower.append(item2)

    for item2 in items_lower:
        if item2[0] > pivot3[0]:
            sub_items_greater2.append(item2)
        else:
            sub_items_lower2.append(item2)
    return sub_items_lower2+[pivot3]+ sub_items_greater2+[pivot]+sub_items_lower+[pivot2]+sub_items_greater