#!/usr/bin/python3
def element_at(my_list, idx):
    for ctr in my_list:
        ctr += 1
    if idx < 0:
        return None
    elif idx > ctr:
        return None
    else:
        return idx + 1
