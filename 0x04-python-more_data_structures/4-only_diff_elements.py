#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    A = [i for i in set_1 if i not in set_2]
    B = [i for i in set_2 if i not in set_1]
    result = A + B
    return(result)
