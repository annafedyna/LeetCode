class Solution:
    '''
        Given an array containing distinct numbers in the range [0, n],
        this function calculates and returns the missing number in the range.
        Parameters:
        - nums (List[int]): The input array of distinct numbers.
        Returns:
        - int: The missing number in the range [0, n].
    '''
    def missingNumber(self, nums: list[int]) -> int:
        sum_n = len(nums)* (len(nums) +1) /2  # expected sum of n elements
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
        return int(sum_n - sum_nums)              
    
    
s = Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))