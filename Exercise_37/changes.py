#!/usr/bin/env python3
"""
    This code implements a change maker
"""
def makeChange(amount):
    """
        This function returns a dictionary with
        change on dollar coins
    """
    change = {}

    if amount >= 25:
        change["quarters"] = amount // 25
        amount = amount % 25
    if amount >= 10:
        change["dimes"] = amount // 10
        amount = amount % 10
    if amount >= 5:
        change["nickels"] = amount // 5
        amount = amount % 5
    if amount > 0:
        change["pennies"] = amount

    return change


# main code
assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
