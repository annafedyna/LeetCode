def maxArea(height: list[int]) -> int:
    max = 0
    pointer1 = 0
    pointer2 = len(height)-1
    
    while pointer1 != pointer2:
        water = ((pointer2+1)-(pointer1+1))*min(height[pointer1], height[pointer2])
        if max < water:
            max = water
        
        if min(height[pointer1], height[pointer2]) == height[pointer1]:
            pointer1 += 1
        else: 
            pointer2 -= 1
    return max
    
print(maxArea([1,8,6,2,5,4,8,3,7]))