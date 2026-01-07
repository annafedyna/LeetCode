def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1 :
        return 2147483647
    nagative = False if (dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0) else True
    res = 0

    if dividend < 0 :
        dividend = (~dividend) + 1
    if divisor < 0:
        divisor = (~divisor) + 1

    i = 0  
    while dividend >= divisor and (divisor << i +1 ) < dividend:
        while (divisor << i +1 ) < dividend:
            i += 1
            
        if i > 0:
            res += (1 << i)
            dividend -=  divisor << i
        i = 0
    
    while dividend >= divisor:
        res += 1
        dividend -= divisor
    
    return (~res) + 1 if nagative else res

print(divide(0, -1))
print(divide(16, 3))
print(divide(2147483647, 1))