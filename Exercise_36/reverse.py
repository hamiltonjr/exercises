#!/usr/bin/env python3
"""
    This code implements the reversion of a string
"""

def reverseString(text):
    if len(text) == "":
        return ""
    
    reversed = ""
    for letter in text:
        reversed = letter + reversed
    return reversed


# main code
assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'
