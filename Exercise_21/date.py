#!/usr/bin/env python3
import datetime

"""
    This code implements a date validation
"""

def isLeapYear(year):
    """
        This function returns if a year is a leap year
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def isValidDate(year, month, day):
    """
        This function returns if a fate is valid
    """
    # validate month in year
    if not (1 <= month <= 12):
        return False
    
    # validate year
    if isLeapYear(year) and month == 2 and day == 29:
        return True
    
    # validate month
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):
        return False
    elif month in (4, 6, 9, 11) and not (1 <= day <= 30):
        return False
    elif month == 2 and not (1 <= day <= 28):
        return False
    
    return True


# main code
assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days = 1)

for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
