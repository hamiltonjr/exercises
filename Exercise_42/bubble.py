#!/usr/bin/env python3
"""
    This code implements the Bubble Sort 
    Algorithm
"""
def bubbleSort(numbers):
    """
        This function returns a list of integer numbers 
        ordered by the Bubble Sort Algorithm
    """
    for i in range(len(numbers) - 1):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


# main code
assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
