class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hash_map = {}
        counter = 0
        for i in range(len(nums)):
            if nums[i] in hash_map.keys():
                counter += hash_map[nums[i]]
                hash_map[nums[i]] += 1
            else: 
                hash_map[nums[i]] = 1
        return counter
    
s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))
