def minimumSum(num: int) -> int:
    s = sorted([*str(num)])
    num1 = [s[i] for i in range(0,len(s),2)]
    num2 = [s[i]  for i in range(1,len(s),2)]
    return int(''.join(num1)) + int(''.join(num2))

print(minimumSum(2932))