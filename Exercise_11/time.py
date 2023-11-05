#!/usr/bin/env python3
"""
    This code implements a seconds converter to
    an hours-minutes-seconds format. I believe that
    my code was better than the templates. I used
    f-strings to create the better solution.
"""
def getHoursMinutesSeconds(seconds):
    """
        This function implements a time converter
    """
    h = int(seconds) // 3600
    m = int(seconds) % 3600
    s = m % 60
    m = m // 60

    result = ""
    if m > 0:
        result = f"{m}m "
    if h > 0:
        result = f"{h}h " + result
    if h + m + s == 0 or s > 0:
        result = result + f"{s}s"
    return result.strip()
    

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
