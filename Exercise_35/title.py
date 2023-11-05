#!/usr/bin/env python3
"""
    This code implements a title case text 
    converter
"""
def getTitleCase(text):
    """
        This function returns a text with the 
        first letter of each word uppercased
    """
    titledText = ""

    for i in range(len(text)):
        if i == 0:
            titledText += text[i].upper()
        elif text[i].isalpha() and not text[i - 1].isalpha():
            titledText += text[i].upper()
        else:
            titledText += text[i].lower()

    return titledText


# main code
assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
