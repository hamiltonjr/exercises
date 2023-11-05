#!/usr/bin/env python3
"""
    This code implements...
"""

def rot13(text):
    encryptedText = ""
    
    for character in text:
        if not character.isalpha():
            encryptedText += character
        else:
            rotatedLetterOrdinal = ord(character) + 13
            if character.islower() and rotatedLetterOrdinal > 122:
                rotatedLetterOrdinal -= 26
            if character.isupper() and rotatedLetterOrdinal > 90:
                rotatedLetterOrdinal -= 26
            encryptedText += chr(rotatedLetterOrdinal)

    return encryptedText

# main code
assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
