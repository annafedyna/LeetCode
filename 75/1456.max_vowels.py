from collections import deque

def maxVowels(s: str, k: int) -> int:
    """ Given a string s and an integer k, 
    return the maximum number of vowel letters in any substring of s with length k"""
    v = ['a','e', 'o', 'i', 'u']
    
    sub = deque(s[:k])
  
    max_vowel = start_vowel = len([i for i in sub if i in v])
    
    p = k
    while p < len(s):
        
        letter = sub.popleft()
        if letter in v:
            start_vowel -= 1
            
        sub.append(s[p])
  
        if s[p] in v:
            start_vowel += 1
        
        if start_vowel > max_vowel:
            max_vowel = start_vowel
     
        p+=1
    return max_vowel
            
print(maxVowels('abciiidef', 3))