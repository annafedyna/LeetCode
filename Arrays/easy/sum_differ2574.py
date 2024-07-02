def leftRightDifference(nums: list[int]) -> list[int]:
    left_sum = [0]
    right_sum = [0]
    answer = []
    
    for i in range(1,len(nums)):
        left_sum.append(nums[i-1]+left_sum[-1])

    for j in range(len(nums)-2, -1, -1):
        right_sum.insert(0, nums[j+1] + right_sum[0])
        
    for g in range(len(nums)):
        answer.append(abs(left_sum[g] - right_sum[g]))

    return answer

print(leftRightDifference([10,4,8,3]))

# 15, 1 ,11, 22