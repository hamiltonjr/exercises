#!/usr/bin/env python3
"""
    This code implements a pyramid drawing
"""

def drawPyramid(height):
    """
        This function draws a simple pyramid
    """
    for i in range(0, height):
        print((height-i-1)*" " + (2*i+1)*"#")


# main code
drawPyramid(5)
