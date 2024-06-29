
def rotate(nums: list[int], k: int):
    n = len(nums)
    k = k % n

    if k == 0:
        return

    memory = {}
    for i in range(k):
        memory[k-1-i] = nums[k-1-i]
        nums[k-1-i] = nums[-i-1]

    if (len(nums) - k) > len(memory):
        for j in range(k, len(nums) - k):
            memory[j] = nums[j]

    for key, value in memory.items():
        if key+k < len(nums):
            nums[key+k] = value
        else:
            nums[abs(len(nums) - (key+k))] = value

    return nums, memory


print(rotate(nums=[-1,-100,3,99], k=3))
