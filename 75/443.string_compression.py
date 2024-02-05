def compress(chars: list[str]) -> int:
    if len(chars) < 2:
        return 1
    
    count = 1
    pointer = 0
    pointer2 = 0
    
    while pointer2 < len(chars)-1:
        if chars[pointer2] != chars[pointer2+1]:
            if count > 1:
                chars[pointer+1: pointer2+1] = list(str(count))
                count = 1
            pointer += len(list(str(count)))
            pointer2 = pointer
        else:
            count += 1
            pointer2 +=1
            if pointer2 == len(chars)-1:
                chars[pointer+1: pointer2+1] = list(str(count))
                
    return len(chars)
            
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))