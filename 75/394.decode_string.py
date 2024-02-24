def decodeString(s: str) -> str:
    stack = []
    news = ''
    i = 0
    while i < len(s):
        if s[i] == '[':
            stack.append(s[i])
            i += 1
            while stack:
                if s[i] == ']' and len(stack) <= 1:
                    stack.pop()
                    d = decodeString(news)
                elif s[i] == ']' and len(stack) > 1:
                    news += s[i]
                    stack.pop()
                elif s[i] == '[':
                    stack.append(s[i])
                    news += s[i]
                else:
                    news += s[i]
                i += 1
        i += 1
    return news

print(decodeString('3[a2[c]]'))

if __name__ == '__main__':
    cases = [
        ('3[a2[c]]','accaccacc'),
        ('2[abc]3[cd]ef','abcabccdcdcdef'),
        ('','')
    ]
    
    # for text, decoded_text in cases:
    #     assert decodeString(text) == decoded_text
