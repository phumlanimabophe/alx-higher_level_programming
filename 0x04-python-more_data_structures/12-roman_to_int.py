#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    int_sum = 0
    converter = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    for i in range(len(roman_string) - 1):
        current = roman_string[i]
        next_ = roman_string[i + 1]

        if converter[current] >= converter[next_]:
            int_sum += converter[current]
        else:
            int_sum -= converter[current]

    int_sum += converter[roman_string[-1]]

    return int_sum
