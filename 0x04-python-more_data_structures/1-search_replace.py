#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for idx in new_list:
        if idx == search:
            new_list[idx] = replace
    return(new_list)
