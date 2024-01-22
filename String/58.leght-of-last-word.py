class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
        
        
s = Solution()
print(s.lengthOfLastWord('  Hello   World  '))