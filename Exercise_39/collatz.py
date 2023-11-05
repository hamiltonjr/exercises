#!/usr/bin/env python3
import random

"""
    This code implemjents the Collatz 
    Algorithm
"""

def collatz(startingNumber):
    if startingNumber < 1:
        return []

    sequence = []
    num = startingNumber
    sequence.append(num)

    while num > 1:
        if num % 2 == 1:
            num = 3*num + 1
        else:
            num = num // 2
        sequence.append(num)
    
    return sequence


# main code
assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1 # Make sure the last integer is 1.
