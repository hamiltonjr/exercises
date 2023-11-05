#!/usr/bin/env python3
"""
    This code implements a number to string converter
"""

def convertIntToStr(integerNum):
    if integerNum == 0:
        return "0"

    if integerNum < 0:
        integerNum = (-1)*integerNum
        isNegative = True
    else:
        isNegative = False

    stringNum = ""
    while integerNum > 0:
        onesPlaceDigit = integerNum % 10
        stringNum = chr(48 + onesPlaceDigit) + stringNum
        integerNum //= 10

    if isNegative:
        return "-" + stringNum
    else:
        return stringNum


# main code
print(convertIntToStr(42379))
print(convertIntToStr(-3245))
