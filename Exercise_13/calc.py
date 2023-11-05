#!/usr/bin/env python3
"""
    This code implements 
"""

def calculateSum(numbers):
    """
        This function returns the sum of
        all values of a list
    """
    if len(numbers) == 0:
        return 0

    sum = 0
    for value in numbers:
        sum = sum + value
    
    return sum


def calculateProduct(numbers):
    """
        This function returns the product of
        all values of a list
    """
    if len(numbers) == 0:
        return 1

    product = 1
    for value in numbers:
        product = product * value
    
    return product


assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
