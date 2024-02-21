'''
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

def longestSubarray(nums: list[int]) -> int:
    
    left = right = longest = zeros = 0

    while right < len(nums):
        if nums[right] == 0:
            zeros += 1
            
        while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
        longest = max(longest, right - left)
        right += 1
        
    return longest         

print(longestSubarray([0,1,1,1,0,1,1,0,1]))
