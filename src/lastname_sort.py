"""
Function for sorting lastname descending
"""

def lastname_sort(final_list):
    l=len(final_list)
    if l <=1:
        return final_list
    else:
        pivot=final_list.pop()
    items_greater=[]
    items_lower = []
    for item in final_list:
        if item[0]<pivot[0]:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return lastname_sort(items_lower)+[pivot]+lastname_sort(items_greater)