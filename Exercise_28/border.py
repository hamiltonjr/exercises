#!/usr/bin/env python3
"""
    This code implements a border drawing
"""

def drawBorder(width, height):
    """
        This function simply draw a border
    """
    print("+" + (width - 2)*"-" + "+")
    for i in range(1, height-1):
        print("|" + (width - 2)*" " + "|")
    print("+" + (width - 2)*"-" + "+")


# main code
drawBorder(16, 4)
