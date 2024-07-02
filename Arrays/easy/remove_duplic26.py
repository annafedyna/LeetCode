class Solution:
    '''
    Removes duplicates in-place from a sorted array. 
    Returns the number of unique elements.

    - nums (List[int]): A sorted list of integers.
    - prev : a pointer to track the position for unique elements
    '''
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        prev = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[prev] = nums[i]
                prev += 1
                
        return prev 