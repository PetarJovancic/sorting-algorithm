"""
Function for sorting datebirth ascending
"""

def datebirth_sort(final_list):
    l=len(final_list)
    if l <=1:
        return final_list
    else:
        pivot=final_list.pop()
    items_greater=[]
    items_lower = []
    for item in final_list:
        if item[3]>pivot[3]:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return datebirth_sort(items_lower)+[pivot]+datebirth_sort(items_greater)