#!/usr/bin/python3
""" 0x0A. 1-my_list """


class MyList(list):
    """Custom list type intended to only contain integers.

    """

    def print_sorted(self):
        """Prints MyList lists in ascending order by value.

        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
