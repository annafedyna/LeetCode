class Solution:
    '''
    Removes all occurrences of a specified value in-place from the given list
    Parameters:
        - nums (List[int]): The input list of integers.
        - val (int): The value to be removed from the list.
    Returns:
    - int: The new length of the list after removing all occurrences of the specified value.
    
    '''
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1             
        return index 
    
s = Solution()
print(s.removeElement([1,2,2,3,0,4],2))