import re

def reverseWords(s:str):
    words = re.findall(r'\w+', s)
    return ' '.join(words[::-1])

print(reverseWords('the sky is blue'))