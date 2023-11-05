#!/usr/bin/env python3
"""
    This code implements reading, appending and
    writing on text files
"""

def writeToFile(filename, text):
    """
        This function saves a text on file
    """
    with open(filename, "w") as fileObj:
        fileObj.write(text)


def appendToFile(filename, text):
    """
        This function appends (saves at the end) 
        a text on file
    """
    with open(filename, "a") as fileObj:
        fileObj.write(text)


def readFromFile(filename):
    """
        This function reads a text to file
        and returns it
    """
    with open(filename) as fileObj:
        return fileObj.read()


writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
