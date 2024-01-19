class Solution:
    '''
    Search for the target in a sorted list of integers and return its index if found.
    If the target is not present, return the index where it would be inserted to maintain sorting.

    Parameters:
    - nums (List[int]): A sorted list of integers.
    - target (int): The integer to search for or insert into the list.
    Returns:
    - int: The index of the target if found; otherwise, the index where the target should be inserted.

    '''
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid +1 
            else: 
                high = mid -1    
            
        return low 
    
s = Solution()
print(s.searchInsert([1,3,5], 7))