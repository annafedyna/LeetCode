def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    '''
    Time Complexity : O(n * n)
    '''
    d ={}
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        d[i] = count
    return [value for key, value in d.items()]

def smallerNumbersThanCurrent2(nums: list):
    '''
    Time Complexity : O(n * logn)
    '''
    sorting = sorted(nums)
    return [sorting.index(i) for i in nums]

print(smallerNumbersThanCurrent2([8,1,2,2,3]))