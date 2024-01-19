class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i, len(nums)):
                    if nums[j] != val:
                       nums[i], nums[j] = nums[j],nums[i]
                
        k = len(nums) - len([i for i in nums if i == val])         
        nums = nums[:k]              
        return k, nums
    
s = Solution()
print(s.removeElement([1,2,2,3,0,4],2))