'''
The pivot index is the index where the sum of all the numbers strictly to the left 
of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 
because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1
'''

def pivotIndex(nums: list[int]) -> int:
    left_sum = [0]
    right_sum = [0]
    
    for i in range(1,len(nums)):
        new_sum = left_sum[-1] + nums[i-1]
        left_sum.append(new_sum)
    
    for i in range(len(nums)-1,0,-1):
        new_sum = right_sum[-1] + nums[i]
        right_sum.append(new_sum)   
        
    right_sum.reverse()
    
    for i in range(len(nums)):
        if left_sum[i] == right_sum[i]:
            return i   
        
    return -1

print(pivotIndex([1,7,3,6,5,6]))