'''
You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

Return the minimum number of operations to make all elements of nums divisible by 3.
'''

def minimumOperations(nums: list[int]) -> int:
    total = 0
    for num in nums:
        if num % 3 != 0:
            total += 1
    return total


print(minimumOperations([1, 2, 3, 4]))
