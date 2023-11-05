#!/usr/bin/env python3
"""
    This code implements the view of the ASCII table
"""

FIRST_CODE = 32
LAST_CODE = 126

def printASCIITable():
    """
        This function implements the ASCII table
        view with header, 5 columns and footer
    """
    columns = 0
    for i in range(FIRST_CODE, LAST_CODE + 1):
        columns = columns + 1
        print(f"{i:3}:{chr(i)}    ", end="")
        
        if columns % 5 == 0:
            columns = 0
            print()


print(14*"=" + " ASCII TABLE " + 14*"=")
printASCIITable()
print(41*"=")
