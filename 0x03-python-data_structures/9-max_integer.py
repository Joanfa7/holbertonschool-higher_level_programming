#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    curr_max = my_list[0]

    for i in my_list:
        if i > curr_max:
            curr_max = i

    return curr_max
