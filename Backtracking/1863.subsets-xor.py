def subsetXORSum(nums: list[int]) -> int:
    sum_ = 0
    subset = []
    
    def dfs(i):
        if i >= len(nums):
            res = 0
            for i in subset:
                res ^= i
            sum_ += res
            return
        
        subset.append(nums[i])
        dfs(i+1)
        
        subset.pop()
        dfs(i+1)
        
    dfs(0)
    return sum_
                