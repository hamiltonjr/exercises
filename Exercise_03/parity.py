#!/usr/bin/env python3
"""
    This code implements parity
"""

def isOdd(number):
    """
        This function says if a number is odd
    """
    return number % 2 != 0


def isEven(number):
    """
        This function says if a number is even
    """
    return number % 2 == 0


# it's must pass
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False

# it is wrong
assert isEven(3.1415) == False
