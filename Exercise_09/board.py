#!/usr/bin/env python3
"""
    This code implements a real-world chess board
    color position verifying
"""

def getChessSquareColor(column, row):
    """
        This function return the color of 
        chess position on a chess board
    """
    if column not in range(1, 9):
        return ''

    if row not in range(1, 9):
        return ''
    
    if column % 2 == row % 2:
        return 'white'
    else:
        return 'black'


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
