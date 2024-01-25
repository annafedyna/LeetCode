def getHint(secret: str, guess: str) -> str:
    d = {}
    x, y = 0, 0
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            x += 1
        else:
            if secret[i] in d.keys():
                d[secret[i]] += 1
            else:
                d[secret[i]] = 1
                
    for j in range(len(guess)):
        if secret[j] != guess[j] and guess[j] in d.keys() :
            if d[guess[j]] != 0:
                y +=1
                d[guess[j]] -= 1
 
    return f'{x}A{y}B'


print(getHint('11','10'))