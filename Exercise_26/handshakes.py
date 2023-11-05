#!/usr/bin/env python3
"""
    This code implements the handshakes combination
    view
"""

def printHandshakes(people):
    numberOfHandshakes = 0
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            print(f"{people[i]} shakes hands with {people[j]}")
            numberOfHandshakes += 1
    print()
    return numberOfHandshakes


# main code
assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
