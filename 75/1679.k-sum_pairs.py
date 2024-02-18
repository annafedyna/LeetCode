from collections import Counter

# O(n)
def maxOperations(nums: list[int], k: int) -> int:
    count = Counter(nums)
    return sum(min(count[num], count[k-num]) for num in nums) //2

print(maxOperations([1,0,4,2],1))