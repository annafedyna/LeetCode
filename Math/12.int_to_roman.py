""" Time: O(13log13)"""

def intToRoman(num: int) -> str:
    int_roman_dict = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    res = ""

    for n in sorted(int_roman_dict.keys(), reverse=True):
        whole_part = num // n
        if whole_part > 0 and whole_part <= 3:
            res += (int_roman_dict[n] * whole_part)
        
        num = num % n

    return res

print(intToRoman(966))