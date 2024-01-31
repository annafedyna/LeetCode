def gcdOfStrings(str1: str, str2: str) -> str: 
    res = ''
    i = min(len(str1), len(str2))
    while i > 0:
        res = str1[:i]
        count1 = len(str1)//(i) if len(str1)%(i) == 0 else 0
        count2 = len(str2)//(i) if len(str2)%(i) == 0 else 0
        if str1 == res * count1 and str2 == res * count2:
            return res
        i -= 1
    return ''
print(gcdOfStrings('NLZGM NLZGM NLZGM NLZGM NLZGM ','NLZGM NLZGM '))