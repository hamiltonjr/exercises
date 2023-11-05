#!/usr/bin/env python3
"""
    This code implements an uppercase text converter. 
    I believe that my code is better than the presented 
    template.
"""

def getUppercase(text):
    """
        This function returns a uppercase version of a text.
        If part of text is already uppercase or is not letters,
        the character is unchanged.
    """
    if text == "":
        return ""
    
    upperCase = ""
    for c in text:
        if 'a' <= c <= 'z':
            upperCase += chr(ord(c) - ord('a') + ord('A'))
        else:
            upperCase += c
    return upperCase


# main code
assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''
