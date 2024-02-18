def maxOperations(nums: list[int], k: int) -> int:
    count = 0
    p1 = 0 
    p2 = 1
    while p1 < p2 and p2<len(nums):
        if nums[p1] + nums[p2] == k:
            count += 1
            del nums[p1] 
            del nums[p2-1]
            p1 = 0 
            p2 = 1
        else:
            p2 += 1 
            if p2 == len(nums):
                p1 += 1
                p2 = p1 + 1
    return count

print(maxOperations([1,0,4,2],15))