
def isSubsequence(s: str, t: str) -> bool:
    for element in t:
        if element  == s[0]:
            s = s[1:]
    return True if not s else False
    
print(isSubsequence('abc', "asdcbc"))