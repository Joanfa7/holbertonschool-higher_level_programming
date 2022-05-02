#!/usr/bin/python3
def no_c(my_string):
    char_to_replace = { 'c' : '',
                        'C' : ''}
    result = ''
    for elem in my_string:
        if elem in char_to_replace:
            result += char_to_replace[elem]
        else:
            result += elem
    return result
