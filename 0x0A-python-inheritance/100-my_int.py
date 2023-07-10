#!/usr/bin/python3
""" 0x0A.100-my_int """


class MyInt(int):
    """Custom int type with inverted behavior for the != and == operators.
    
    """


    def __eq__(self, other):
        """Reverses behavior of == operator.

        """
        return int(self) != int(other)

    def __ne__(self, other):
        """Reverses behavior of != operator.

        """
        return int(self) == int(other)
