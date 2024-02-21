def longestOnes(nums: list[int], k: int) -> int:
    longest = 0
    index = 0
    zeros = k
    count = 0
    
    while index < len(nums):
        count += 1
        if nums[index] == 0:
            zeros -= 1
            while zeros < 0:
                if nums[index-count+1] == 0:
                    zeros += 1
                count -= 1
           
        index += 1 
    return longest

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))