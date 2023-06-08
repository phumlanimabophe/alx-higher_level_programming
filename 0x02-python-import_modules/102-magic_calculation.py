#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        answer = add(a, b)
        for i in range(4, 6):
            answer = add(answer, i)
        return answer

    else:
        return sub(a, b)
