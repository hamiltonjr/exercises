#!/usr/bin/env python3
"""
    This code implements
"""

def findAndReplace(text, oldText, newText):
    """
        This function implements a find-and-replace using
        string slicing
    """
    replacedText = ""
    i = 0

    while i < len(text):
        if text[i:i+len(oldText)] == oldText:
            replacedText = replacedText + newText
            i = i + len(newText)
        else:
            replacedText = replacedText + text[i]
            i = i + 1
    
    return replacedText


assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
