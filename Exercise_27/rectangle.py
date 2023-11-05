#!/usr/bin/env python3
"""
    This code implenments a rectangle drawing
"""

def drawRectangle(width, height):
    """
        This function returns a rectangle with width
        # signs in height lines
    """
    if width < 1 or height < 1:
        return

    while height > 0:
        print(width*"#")
        height = height - 1


# main code
drawRectangle(16, 4)
