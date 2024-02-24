def decodeString(s: str) -> str:
    stack = []
    sub = ''
    i = 0
    num = ''
    while i < len(s):
        while s[i].isdigit():
            num += s[i]
            i += 1
        if num != '': stack.append(int(num))
        num = ''
        
        if s[i] == ']':
            while stack[-1] != '[' :
                sub = stack.pop() + sub
            stack.pop()
            n = stack.pop()
            stack.append(n * sub)
            sub = ''
        else: 
            stack.append(s[i])
        i +=1       
    return ''.join(stack)

print(decodeString('3[a2[c]]'))

if __name__ == '__main__':
    cases = [
        ('3[a2[c]]','accaccacc'),
        ('2[abc]3[cd]ef','abcabccdcdcdef'),
        ('','')
    ]
    
    for text, decoded_text in cases:
        assert decodeString(text) == decoded_text
