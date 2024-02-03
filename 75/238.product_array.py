def productExceptSelf(nums: list[int]) -> list[int]:
    res = []
    prefix = [nums[0]]
    suffix = [nums[-1]]
    
    for i in range(1,len(nums)-1):
        prefix.append(prefix[-1]*nums[i])
    
    for i in range(len(nums)-2, 0, -1):
        suffix.append(suffix[-1]*nums[i])
     
    res.append(suffix[-1])    
    for j in range(0, len(prefix)-1):
        res.append(prefix[j]*suffix[len(suffix)-2-j])
    res.append(prefix[-1])
    
    return res
    
print(productExceptSelf([1,2,3,4]))