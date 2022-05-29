#!/usr/bin/python3
""" Returns True if the object is a n instancce of,
    or if if the object is an instance of a class that inherited
    from the specifiied class; otherwise False"""


def is_kind_of_class(obj, a_class):
    """ check instance or intherence """
    
    if isinstance(obj, a_class):
        return True
    else:
        return False
