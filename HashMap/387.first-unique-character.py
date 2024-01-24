def firstUniqChar(s: str) -> int:
    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    d = {}
    for i in range(len(s)):
        char = s[i]
        if char in d.keys():
            d[char] += 1
        else:
            d[char] = 1
    for i in list(d.items()):
        if i[1] == 1:
            return s.index(i[0])
    return -1
        
        
    

print(firstUniqChar('aadadaadcd'))