#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

l_dgt = (number % 10)

if l_dgt > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, l_dgt))

elif l_dgt == 0:
    print("Last digit of {} is {}".format(number, l_dgt))

elif l_dgt < 6 and last_digit != 0:
    print("Last digit of {} is {:-d} and is less than 6 and not 0"
          .format(number, l_dgt))
