'''
Time Complexity: O(n^2)
Space Complexity: O(n)
'''
def predictPartyVictory(senate: str) -> str:
    q = list(senate)
    d_count = 0
    r_count = 0

    while ('R' in q) and ('D' in q):
        new_q = []
        for element in q[:]:
            if element == 'D':
                if r_count > 0:
                    r_count -= 1  
                else:
                    new_q.append('D')
                    d_count += 1
            elif element == 'R':
                if d_count > 0:
                    d_count -= 1
                else:
                    new_q.append('R')
                    r_count += 1
        q = new_q
    
    return 'Radiant' if  'R' in q else 'Dire'
    
# print(predictPartyVictory('DDDDRRDDDRDRDRRDDRDDDRDRRRRDRRRRRDRDDRDDRRDDRRRDDRRRDDDDRRRRRRRDDRRRDDRDDDRRRDRDDRDDDRRDRRDRRRDRDRDR'))

if __name__ == '__main__':
    cases = [
        ('RD','Radiant'),
        ('RDD','Dire'),
        ('DDRRR','Dire'),
        ('DDDDRRDDDRDRDRRDDRDDDRDRRRRDRRRRRDRDDRDDRRDDRRRDDRRRDDDDRRRRRRRDDRRRDDRDDDRRRDRDDRDDDRRDRRDRRRDRDRDR', 'Dire')
    ]
    
    for text, decoded_text in cases:
        assert predictPartyVictory(text) == decoded_text
