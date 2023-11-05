#!/usr/bin/env python3
"""
    This code implements coffe buying with promo. I believe that my code is netter than the presented template.
"""

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    if numberOfCoffees % 8 >= 1:
        numberOfCoffees -= numberOfCoffees // 8
    return pricePerCoffee * numberOfCoffees


# main code
assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i
