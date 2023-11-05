#!/usr/bin/env python3
"""
    This code implemenmts a multiplication table
"""

print("   |  1   2   3   4   5   6   7   8   9  10")
print("---+---------------------------------------")

for i in range(1, 11):
    print(f"{i:>2} | ", end="")
    for j in range(1, 11):
        print(f"{i*j:>2}  ", end="")
    print()
