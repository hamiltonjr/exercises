#!/usr/bin/env python3
"""
    This code implements the FizzVuzz joke
"""

def fizzBuzz(upTo):
    """
        This function impmenets the FizzBuzz joke
    """
    for number in range(1, upTo+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
    print()


fizzBuzz(6)
fizzBuzz(10)
fizzBuzz(11)
fizzBuzz(15)
