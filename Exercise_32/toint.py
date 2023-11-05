#!/usr/bin/env python3
"""
    This code implements conversion from string to integer
"""

def convertStrToInt(stringNum):
    """
        This function returns an integer like its
        string trptrsentation
    """
    if stringNum == "0":
        return 0

    if stringNum[0] == "-":
        isNegative = True
        stringNum = stringNum[1:]
    else:
        isNegative = False

    integerNum = 0
    for i in range(len(stringNum)-1, -1, -1):
        integerNum += (ord(stringNum[i]) - ord('0')) * 10**(len(stringNum) - i - 1)
    
    if isNegative:
        return -integerNum
    return integerNum


# main code
print(convertStrToInt('123'))
print(convertStrToInt('42097'))
print(convertStrToInt('-209'))
