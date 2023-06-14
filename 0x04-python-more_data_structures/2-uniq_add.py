#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_set = set(my_list)
    for a in my_set:
        sum += a
    return sum
