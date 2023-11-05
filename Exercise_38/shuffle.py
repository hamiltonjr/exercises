#!/usr/bin/env python3
import random

"""
    This code implements a random shuffle of
    a list of integer numbers
"""

def shuffle(values):
    """
        This function returns the list with
        its values shuffled
    """
    if len(values) == 0:
        return []
    
    length = len(values)

    for i in range(length):
        index = random.randint(0, length-1)
        values[i], values[index] = values[index], values[i]

    return values


# main code
random.seed(42)
# Perform this test ten times:
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)

    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10

    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []
