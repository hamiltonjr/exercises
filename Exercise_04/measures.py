#!/usr/bin/env python3
"""
    This is a measuring test code
"""

def area(w, h):
    """
        This function returns the area, given
        width and hwight
    """
    return w * h


def perimeter(w, h):
    """
        This function returns the perimeter, given
        width and hwight
    """
    return 2*(w + h)


def volume(w, h, d):
    """
        This function returns the volume, given
        width, hwight and depth
    """
    return w * h * d


def surfaceArea(w, h, d):
    """
        This function returns the surface area, given
        width, hwight and depth
    """
    return 2 * (w*h + w*d + h*d)


# all asserts are correct
assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340
