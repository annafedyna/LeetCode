def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    d ={}
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        d[i] = count
    return [value for key, value in d.items()]


print(smallerNumbersThanCurrent([8,1,2,2,3]))