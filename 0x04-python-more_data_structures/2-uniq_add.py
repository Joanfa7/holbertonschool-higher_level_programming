#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(my_list)
    unique = []
    for num in new_list:
        if num in unique:
            continue
        else:
            unique.append(num)
    result = sum(unique)
    return(result)
