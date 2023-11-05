#!/usr/bin/env python3
"""
    This code implements the median calculation
"""

def median(numbers):
    """
        This function returns the median of
        a list of values
    """
    if len(numbers) == 0:
        return None
    
    numbers.sort()
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle] + numbers[middle-1]) / 2
    else:
        return numbers[middle]


# main code
import random
random.seed(42)

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6
