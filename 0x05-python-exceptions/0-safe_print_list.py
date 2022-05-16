#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ctr = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            ctr += 1
        except:
            continue

    print()
    return(ctr)
