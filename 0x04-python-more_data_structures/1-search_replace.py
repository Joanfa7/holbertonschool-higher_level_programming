#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for idx in new_list:
        if idx == search:
            new_list[idx] = replace
    print(new_list)
