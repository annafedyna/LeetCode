
def predictPartyVictory(senate: str) -> str:
    q = list(senate)
    d = {'D': 0, 'R': 0}
    i = 0
    d_count =0 
    r_count = 0
    
    while i < len(senate):
        element = q.pop(0)
        if element == 'D' and r_count == 0:
            d['D'] += 1
            d_count += 1
        elif element == 'R' and d_count == 0:
            d['R'] += 1
            r_count += 1
        elif element == 'D' and r_count != 0:
            r_count -= 1
        else:
            d_count -= 1
        i += 1
        
    if d['D'] > d['R']:
        return 'Dire'
    elif d['D'] < d['R']:
        return 'Radiant'
    
    return 'Radiant' if senate[-1] == 'R' else 'Dire'
    
print(predictPartyVictory('RDD'))

if __name__ == '__main__':
    cases = [
        ('RD','Radiant'),
        ('RDD','Dire'),
        ('DDRRR','Dire')
    ]
    
    for text, decoded_text in cases:
        assert predictPartyVictory(text) == decoded_text

