#!/usr/bin/env python3
import random

"""
    This code implements a password generator
"""

LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL = "~!@#$%^&*()_+"

def generatePassword(length):
    """
        Tgis function sorts one of each mandatory characters and then freely sorts the others,
        compounding a given LENGTH width string as a generated password 
    """
    # all characters
    ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

    # minimum length
    if length < 12:
        length = 12

    # mandatory characters sorted first
    password = []
    password.append(LOWER_LETTERS[random.randint(0, 
    len(LOWER_LETTERS) - 1)])
    password.append(UPPER_LETTERS[random.randint(0, len(UPPER_LETTERS) - 1)])
    password.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
    password.append(SPECIAL[random.randint(0, len(SPECIAL) - 1)])

    # freely sorted characters after
    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, len(ALL_CHARS) - 1)])

    # shuffle the characters
    random.shuffle(password)

    # return generated password as a string that has
    # the wanted format
    return "".join(password)

        
# main code
assert len(generatePassword(8)) == 12

pw = generatePassword(14)
assert len(pw) == 14

hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False

for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial
