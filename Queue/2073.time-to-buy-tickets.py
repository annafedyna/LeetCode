def timeRequiredToBuy(tickets: list[int], k: int) -> int:
    '''
    Time Complexity: O(m*n), m = max(tickets[i])
    Space Complexity : O(n)
    '''
    time = 0
    while tickets[k]:
        for i in range(len(tickets)):
            if tickets[i] !=0:
                tickets[i] -= 1
                time += 1 
            if tickets[k] == 0:
                break
        print(tickets, time)
    return time

def timeRequiredToBuy2(tickets: list[int], k: int) -> int:
    '''
    Time Complexity: O(n)
    Space Complexity : O(1)
    '''
    time = 0
    for i in range(k):
        time += min(tickets[i], tickets[k])
    for j in range(k+1,len(tickets)):
        time += min(tickets[j], tickets[k]-1)
    return time + tickets[k]


print(timeRequiredToBuy2([84, 49, 5, 24, 70, 77, 87, 8],3))