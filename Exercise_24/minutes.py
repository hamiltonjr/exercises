#!/usr/bin/env python3

# main code
for meridiem in ["am", "pm"]:
    for hour in ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
        for minutes in ["00", "15", "30", "45"]:
            print(f"{hour:>2}:{minutes:2} {meridiem}")
