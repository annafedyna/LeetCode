def shuffle(nums: list[int], n: int) -> list:
    shuffled_list = []
    
    for i in range(n):
        j = i 
        while j < len(nums): 
            shuffled_list.append(nums[j])
            j += n
    return shuffled_list
    
print(shuffle([2,5,1,3,4,7], 3))