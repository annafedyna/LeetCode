def reverseVowels(s: str) -> str:
    vowels = ['a', 'o', 'u', 'e', 'i', 'A','O', 'U', 'E', 'I' ]
    pointer1 = 0
    pointer2 = len(s)-1
    slist = list(s)
    
    while pointer2 >= pointer1:
        if slist[pointer1] in vowels and slist[pointer2] in vowels:
            slist[pointer1], slist[pointer2] = slist[pointer2],slist[pointer1]
            pointer1 += 1 
            pointer2 -= 1
        elif slist[pointer1] in vowels and slist[pointer2] not in vowels:
            pointer2 -= 1
        elif slist[pointer1] not in vowels and slist[pointer2] in vowels:
            pointer1 += 1
        else:
            pointer1 += 1 
            pointer2 -= 1
    return ''.join(slist)

print(reverseVowels('hello'))