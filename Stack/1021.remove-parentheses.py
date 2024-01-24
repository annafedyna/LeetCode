def removeOuterParentheses(s: str) -> str:
    stack = []
    res = []
    for i in range(0,len(s)):
        if s[i] == '(':
            if not stack:
                stack.append(s[i])
            else:
                res.append(s[i]) 
                stack.append(s[i])      
        else:
            if stack[-1] == '(':
                stack.pop()
                if stack:
                    res.append(')')
    return ''.join(res)
    
print(removeOuterParentheses('(()())(())(()(()))'))