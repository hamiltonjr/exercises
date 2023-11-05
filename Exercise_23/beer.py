#!/usr/bin/env python3
"""
    This code implements the 99 berrs song
"""

def beers(numberOfBottles):
    """
        This function returns a part of the beer's song
    """
    verse = f"{numberOfBottles} bottles of beer on the wall,\n"
    verse += f"{numberOfBottles} bottles of beer,\n"
    verse += "Take one down\nPass it around,\n"
    if numberOfBottles == 1:
        verse += "No more bottles of beer on the wall!\n"
    else:
        verse += f"{numberOfBottles-1} bottles of beer on the wall,\n\n"
    return verse


# main code: the loop uses the function to write the entire song
for i in range(99, 0, -1):
    print(beers(i))    
