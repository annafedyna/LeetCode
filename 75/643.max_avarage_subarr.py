def findMaxAverage(nums: list[int], k: int) -> float:
    max_sum = sum(nums[i] for i in range(k))
    
    if k < len(nums):
        new_sum = max_sum
        for i in range(k,len(nums)):
            new_sum = new_sum - nums[i-k] + nums[i]
            
            if new_sum > max_sum:
                max_sum = new_sum
    return max_sum 
        

print(findMaxAverage([0,4,0,3,2], 1))