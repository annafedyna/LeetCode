'''
The biker starts his trip on point 0 with altitude equal 0.
gain: int - of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point
'''

def largestAltitude(gain: list[int]) -> int:
    highest = 0
    prefix_sum = 0
    
    for i in range(len(gain)):
        prefix_sum += gain[i]
        highest = max(prefix_sum,highest)
    return highest

print(largestAltitude([-5,1,5,0,-7]))