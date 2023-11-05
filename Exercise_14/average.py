#!/usr/bin/env python3
"""
    This code implements average calculation
"""

def average(numbers):
    """
        This function return s the average 
        of values of a list
    """
    if len(numbers) == 0:
        return None
    
    sum = 0
    for value in numbers:
        sum = sum + value
    return sum / len(numbers)


import random
random.seed(42)

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2
