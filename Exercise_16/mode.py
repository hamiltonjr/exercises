#!/usr/bin/env python3
"""
    This code implements the mode of a list
"""
def mode(numbers):
    """
        This functiom returns the mode of a list
    """
    if len(numbers) == 0:
        return None
    
    numberCount = {}
    mostFreqNumber = None
    mostFreqNumberCount = 1

    for number in numbers:
        if number not in numberCount:
            numberCount[number] = 1
        numberCount[number] += 1
        if numberCount[number] > mostFreqNumberCount:
            mostFreqNumber = number
            mostFreqNumberCount = numberCount[number]
    return mostFreqNumber


# main code
import random
random.seed(42)

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
