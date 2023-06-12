#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    v1 = tuple_a or (0, 0)
    v2 = tuple_b or (0, 0)
    if len(tuple_a) == 1:
        v1 = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        v2 = (tuple_b[0], 0)
    new = (v1[0] + v2[0], v1[1] + v2[1])
    return new
