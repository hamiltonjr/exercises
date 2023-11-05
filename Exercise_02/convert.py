#!/usr/bin/env python3
"""
    This is a simple temperature converter
"""

def convertToCelsius(t):
    """
        This function converts temperature in Fahrenheit
        to Celsius degrees
    """
    return 5*(t - 32)/9


def convertToFahrenheit(t):
    """
        This function converts temperature in Celsius
        to Fahrenheit degrees 
    """
    return 9*t/5 + 32


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

# Rounding errors cause a slight discrepancy:
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
