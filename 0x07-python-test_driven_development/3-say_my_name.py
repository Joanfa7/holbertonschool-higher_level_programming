#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Function that print the fist and last name of a person."""


    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

