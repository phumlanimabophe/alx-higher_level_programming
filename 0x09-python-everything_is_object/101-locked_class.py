#!/usr/bin/python3
"""class with predefined number of slots"""


class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))