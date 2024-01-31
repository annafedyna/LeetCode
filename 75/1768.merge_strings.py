from collections import deque

def mergeAlternately(word1: str, word2: str) -> str:
    w1 = deque(word1)
    w2 = deque(word2)
    res = []
    while len(w1) != 0 or len(w2)!= 0:
        if w1 and w2:
            res.append(w1.popleft())
            res.append(w2.popleft())
        elif w1 and not w2:
            res.append(w1.popleft())
        else:
            res.append(w2.popleft())

    return ''.join(res)

print(mergeAlternately('abcd', 'prt'))