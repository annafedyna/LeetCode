def compress(chars: list[str]) -> int:
    res = 0
    pointer1 = 0
    pointer2 = 0
    
    count = 0
    while pointer2 < len(chars):
        letter = chars[pointer1]
        count = 0
        
        while pointer2 < len(chars) and chars[pointer2] == letter:
            count += 1
            pointer2 += 1
        
        chars[res] = letter
        res += 1
        if count > 1:
            for num in str(count):
                chars[res] = num
                res += 1    
            
        pointer1 = pointer2 
        
    return res
            
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b",'c']))