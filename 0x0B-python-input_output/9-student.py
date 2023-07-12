#!/usr/bin/python3
"""Student"""


class Student:
    """Simple class containing student data.

    Args:
        first_name (str): given name of student
        last_name (str): family name of student
        age (int): age of student in years

    Attributes:
        first_name (str): given name of student
        last_name (str): family name of student
        age (int): age of student in years

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

