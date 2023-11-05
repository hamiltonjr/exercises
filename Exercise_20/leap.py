#!/usr/bin/env python3

"""
    This code implements leap year verifying
"""

def isLeapYear(year):
    """
        This function returns if a year is a leap year
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# main code
# assert isLeapYear(1999) == False
# assert isLeapYear(2000) == True
# assert isLeapYear(2001) == False
# assert isLeapYear(2004) == True
# assert isLeapYear(2100) == False
# assert isLeapYear(2400) == True
