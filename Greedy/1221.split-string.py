def balancedStringSplit(s: str) -> int:
    substring_amount = 0
    r_amount= 0
    l_amount = 0
    for char in s:
        if char == 'R':
            r_amount += 1
        else:
            l_amount += 1
        if r_amount == l_amount:
            substring_amount += 1
            
    return substring_amount
             

print(balancedStringSplit("RLRRRLLLRLL"))