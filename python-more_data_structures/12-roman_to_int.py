#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num = 0

    for i in range(len(roman_string)):
        if roman_d.get(roman_string[i], 0) == 0:
            return 0
        if (i < len(roman_string) - 1 and
                roman_d[roman_string[i]] < roman_d[roman_string[i + 1]]):
            num -= roman_d[roman_string[i]]
        else:
            num += roman_d[roman_string[i]]

    return num
