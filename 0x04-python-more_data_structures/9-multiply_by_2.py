#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    for value in new_list:
        new_list[value] = new_list[value] * 2
    return(new_list)
