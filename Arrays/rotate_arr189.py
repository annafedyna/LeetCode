
def rotate(nums: list[int], k: int):
    memory = {}
    for i in range(k):
        memory[k-1-i] = nums[k-1-i]
        nums[k-1-i] = nums[-i-1]
        
    if (len(nums) - k) > len(memory):
        for j in range(k, len(nums) - k ):
            memory[j] = nums[j]

    for key, value in memory.items():
        nums[key+k] = value
        
    return nums, memory


print(rotate(nums=[1, 2, 3, 14, 15, 16, 17], k=3))
